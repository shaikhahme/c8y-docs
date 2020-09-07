---
weight: 80
title: Device certificates (beta)
layout: redirect
---

### Overview

Devices can authenticate against the Cumulocity IoT platform using X.509 client certificates.  

Devices can communicate using the MQTT interface of the platform, but MQTT over WebSocket is not supported. The Cumulocity IoT platform expects devices to connect using SSL on port 1884.

Each tenant individually defines whom it trusts by uploading the base CA certificate.

Devices connecting to the platform with certificates do not need to provide the tenant ID, username and password. Authentication information will be obtained from the certificates.

#### General requirements for connecting devices with certificates

* The CA certificate may also be a self-signed certificate.
* Certificates used by devices must be a full chain, including the uploaded CA certificate.
* The device needs to trust the Cumulocity IoT certificate.
* Uploaded certificates have to be version 3.
* Uploaded certificates have to have set `BasicConstraints:[CA:true]`.
* Devices have to be registered or the uploaded certificates need to have the flag _autoRegistrationEnabled_ (see below for details).
* Certificates used by devices must be signed either by uploaded CA certificates or by a chain of certificates signed by uploaded CA certificates.

### Registering devices using certificates

Cumulocity IoT supports two ways to register devices which will be able to connect using certificates:

**Auto registration**

The user for the device will be created during the first MQTT call, if at least one uploaded certificate has _autoRegistrationEnabled_ set to true.

**Bulk registration**

The user for the device can also be created via the standard bulk registration in Device Management.

The CSV file used in bulk registration should meet the requirements described in [Bulk device credentials](/reference/device-credentials/#bulk-device-credentials) in the *Reference guide*. Moreover, it is required that the CSV file has an additional column "AUTH_TYPE" with value "CERTIFICATES", and that the column "CREDENTIALS" is either not present or has an empty value.

### JWT Token retrieval

A device which is connected by certificates can receive a token which can later be used to authenticate HTTP requests. Note that [JWT token authentication](/reference/rest-implementation/#http-usage) must be enabled to receive a token.

* First the device subscribes to the topic <kbd>s/dat</kbd>.
* Then the device publishes an empty message on the topic <kbd>s/uat</kbd>.
* After a while a token will be published on the subscribed <kbd>s/dat</kbd> topic in the format:

```plain
71,<<Base64 encoded JWT token>>
```