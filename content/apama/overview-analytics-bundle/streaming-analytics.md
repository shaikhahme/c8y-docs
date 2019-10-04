---
weight: 10
title: Streaming analytics with Apama EPL
layout: redirect
---
Using Apama streaming analytics, you can add your own logic to your IoT solution for immediate processing of incoming data from devices or other data sources. These user-defined operations can, for example, alert applications of new incoming data, create new operations based on the received data (such as sending an alarm when a threshold for a sensor is exceeded), or trigger operations on devices.

The operation logic is based on Apama's Event Processing Language (Apama EPL).

>**Important**: Support for streaming analytics using CEL (Esper) is deprecated. All new Cumulocity IoT subscriptions use the Apama CEP engine. While using the Esper CEP engine is still supported for older installations, this will no longer be provided for new subscriptions and will not be invested into in the future. 
>
>For documentation on using the deprecated CEL functionality based on Esper, refer to the [CEL analytics guide](/guides/event-language/introduction). 
>
>For details on migration, see [Migrating from CEL (Esper) to Apama](#migrate-from-esper).


Typical real-time analytics use cases include:

* Remote control: Turn a device off if its temperature rises over 40 degrees.
* Validation: Discard negative meter readings or meter readings that are lower than the previous.
* Derived data: Calculate the volume of sales transactions per vending machine per day.
* Aggregation: Sum up the sales of vending machines for a customer per day.
* Notifications: Send me an email if there is a power outage in one of my machines.
* Compression: Store location updates of all cars only once every five minutes (but still send real-time data for the car that I am looking at to the user interface).

The following sections describe the basics for understanding how Apama EPL works and how you can create your own analytics or other server-side business logic and automation.

>**Info**: This documentation assumes basic familiarity with Apama application development. Refer to the [Apama documentation](https://documentation.softwareag.com/onlinehelp/Rohan/Apama/v10-5/apama10-5/apama-webhelp/) for further details.