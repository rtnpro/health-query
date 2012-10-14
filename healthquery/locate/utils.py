# -*- coding: utf-8 -*-
from __future__ import absolute_import
import re
from healthquery.people.models import DoctorLocation
from django.contrib.gis.geos import *


def parse_query_string(query_string):
    """
    Return a lookup dict
    "doctors for disease foo"
    "doctors with specialization foo"
    """
    doctors_disease_regex = re.compile(
        r'doctors for disease (?P<disease>\w+)')
    doctors_specialities_regex = re.compile(
        r'doctors speciali(?:z|s)ed in (?P<specialization>\w+)')
    m1 = doctors_disease_regex.match(query_string)
    m2 = doctors_specialities_regex.match(query_string)
    if m1:
        return {
            'lookup': 'doctors',
            'specializations': Specialization.objects.for_disease(
                Disease.objects.filter(name__in=m1.groups('disease'))
        }
    elif m2:
        return {
            'lookup': 'doctors',
            'specializations': Specialization.objects.by_name_or_alias(
                m2.groups('specialization'))
        }


def search_from_query(query_string, location):
    formatted_query = parse_query_string(query_string)
    results = []
    if formatted_query.get('lookup') == 'doctors':
        results = find_nearby_doctors(
            location, formatted_query['specializations'])
    elif formatted_query.get('lookup') == 'places':
        results = find_nearby_places(
            location, formatted_query['specializations'])
    return results


def local_search(query):
    pass


def google_places_search(query):
    pass


def get_geopoint_from_location_tuple(location):
    return fromstr('POINT(%s %s)' % (location[0], location[1]), srid=4326)


def get_formatted_doctor_results(qs):
    results = []
    for place in qs:
        results.append({
            'formatted_address': place.formatted_address,
            'geometry': {
                'location': {
                    'lat': place.geometry.latLng[0],
                    'lng': place.geometry.latLng[1]
                }
            },
            'icon': place.icon,
            'id': place.google_places_id,
            'name': place.doctor.name,
            'rating': place.rating,
            'reference': place.google_places_refid,
            'types': types_as_list(place.types)
        })
    return results


def types_as_list(types_str):
    return [t for t in types_str.split(',') if t]


def get_formatted_place_results(qs):
    results = []
    for place in qs:
        results.append({
            'formatted_address': place.formatted_address,
            'geometry': {
                'location': {
                    'lat': place.geometry.latLng[0],
                    'lng': place.geometry.latLng[1]
                }
            },
            'icon': place.icon,
            'id': place.google_places_id,
            'name': place.name,
            'rating': place.rating,
            'reference': place.google_places_refid,
            'types': types_as_list(place.types)
        })
    return results


def get_formatted_results(qs, category='place'):
    if category == 'doctor':
        return get_formatted_doctor_results(qs)
    elif category == 'place':
        return get_formatted_place_results(qs)
    return []


def find_nearby_doctors(location, specializations=[],
    radius=50000):
    pnt = get_geopoint_from_location_tuple(location)
    return get_formatted_results(DoctorLocation.objects.filter(
        doctor__specializations=specializations,
        place__geometry__distance_lte=(pnt, radius)), category='doctor')


def find_nearby_places(location, specializations=[], radius=50000):
    pnt = get_geopoint_from_location_tuple(location)
    return get_formatted_results(Place.objects.filter(
        specializations=specializations,
        geometry__distance_lte=(pnt, radius)), category='place')


