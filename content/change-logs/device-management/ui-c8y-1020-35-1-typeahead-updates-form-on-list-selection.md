---
date: ""
title: Typeahead component now updates form when selecting an item from the list
product_area: Device management & connectivity
change_type:
  - value: change-VSkj2iV9m
    label: Fix
component:
  - value: component--KIsStyzM
    label: Device Management app
build_artifact:
  - value: tc-pjJiURv9Y
    label: ui-c8y
ticket: DM-3877
version: 1020.35.1
---
The typeahead component allows users to quickly find and select an item from a list as they type. Previously, when a user selected an item from the typeahead list, the form would not update with the selected value. This could lead to confusion if the user thought they had selected a value but it was not actually set in the form. Now, when a user selects an item from the typeahead list, the associated form field will be immediately updated with the selected value. This provides a clearer and more intuitive user experience when using typeahead fields in forms.