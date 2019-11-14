# Overview

This Python script will iterate over a REST endpoint, enumerate all of the IDs, and exit displaying an error message if a duplicate is found.

It is useful for identifiying issues where a default ordering is not set on a model, or if an attribute is not added to `ordering_fields`.

