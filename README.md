# CityDataBox

### Simple RESTful API that provides information about cities. It is designed to be easy to use with a simple JSON-based interface that returns data in a standardized format.
#
## API Documentation

This API provides access to information about cities. The following endpoints are available:

### 1. Retrieve information about a city with the specified name

**Endpoint:** `/city/name`

**HTTP Method:** GET

**Description:** Retrieves information about a city with the specified name.

**Parameters:**

- name (string)

**Example Request:**

```
GET /city/new york
```

**Example Response:**

```json
{
	"admin_name": "New York",
	"capital": "",
	"city": "New York",
	"city_ascii": "New York",
	"country": "United States",
	"id": 12,
	"iso2": "US",
	"iso3": "USA",
	"lat": "40.6943",
	"lng": "-73.9249",
	"population": "18972871"
}
```

### 2. Retrieve a list of all cities in the database

**Endpoint:** `/cities`

**HTTP Method:** GET

**Description:** Retrieves a list of all cities in the database (max result = 100 per page).

**Example Request:**

```
GET /cities
```

**Example Response:**

```json
{
	"data": [
		{
			"admin_name": "Tokyo",
			"capital": "primary",
			"city": "Tokyo",
			"city_ascii": "Tokyo",
			"country": "Japan",
			"id": 1,
			"iso2": "JP",
			"iso3": "JPN",
			"lat": "35.6897",
			"lng": "139.6922",
			"population": "37732000"
		},
		{
			"admin_name": "Jakarta",
			"capital": "primary",
			"city": "Jakarta",
			"city_ascii": "Jakarta",
			"country": "Indonesia",
			"id": 2,
			"iso2": "ID",
			"iso3": "IDN",
			"lat": "-6.175",
			"lng": "106.8275",
			"population": "33756000"
		}
   ...
],
	"page": 1,
	"total_data": 44691,
	"total_pages": 447
}
```

### 3. Retrieve a list of cities by a specified country name

**Endpoint:** `/country/name`

**HTTP Method:** GET

**Description:** Retrieve a list of cities with specified  country name (max result = 100 per page).

**Parameters:**

- name (string)

**Example Request:**

```
GET /country/spain
```

**Example Response:**

```json
{
	"data": [
		{
			"admin_name": "Madrid",
			"capital": "primary",
			"city": "Madrid",
			"city_ascii": "Madrid",
			"country": "Spain",
			"id": 89,
			"iso2": "ES",
			"iso3": "ESP",
			"lat": "40.4169",
			"lng": "-3.7033",
			"population": "6211000"
		},
		{
			"admin_name": "Catalonia",
			"capital": "admin",
			"city": "Barcelona",
			"city_ascii": "Barcelona",
			"country": "Spain",
			"id": 151,
			"iso2": "ES",
			"iso3": "ESP",
			"lat": "41.3825",
			"lng": "2.1769",
			"population": "4800000"
		}
      ...
   ],

   "page": 1,
	"total_data": 754,
	"total_pages": 8
}
```

### 4. Retrieve information about a city with the specified ID

**Endpoint:** `/city/id`

**HTTP Method:** GET

**Description:** Retrieves information about a city with the specified ID.

**Parameters:**

- id (integer)

**Example Request:**

```
GET /city/2
```

**Example Response:**

```json
{
	"admin_name": "Jakarta",
	"capital": "primary",
	"city": "Jakarta",
	"city_ascii": "Jakarta",
	"country": "Indonesia",
	"id": 2,
	"iso2": "ID",
	"iso3": "IDN",
	"lat": "-6.175",
	"lng": "106.8275",
	"population": "33756000"
}
```

### 5. Retrieve information about a country with the specified ISO 3166-1 alpha-3 code

**Endpoint:** `/country/iso3/name`

**HTTP Method:** GET

**Description:** Retrieves information about a country with the specified ISO 3166-1 alpha-3 code.

**Parameters:**

- iso3 (string): the ISO 3166-1 alpha-3 code of the country (e.g. USA)

**Example Request:**

```
GET /country/iso3/USA
```

**Example Response:**

```json
{
	"data": [
		{
			"admin_name": "New York",
			"capital": "",
			"city": "New York",
			"city_ascii": "New York",
			"country": "United States",
			"id": 12,
			"iso2": "US",
			"iso3": "USA",
			"lat": "40.6943",
			"lng": "-73.9249",
			"population": "18972871"
		},
		{
			"admin_name": "California",
			"capital": "",
			"city": "Los Angeles",
			"city_ascii": "Los Angeles",
			"country": "United States",
			"id": 34,
			"iso2": "US",
			"iso3": "USA",
			"lat": "34.1141",
			"lng": "-118.4068",
			"population": "12121244"
		},
      ....
	],
	"page": 1,
	"total_data": 5393,
	"total_pages": 54
}
```
Note: The ISO 3166-1 alpha-3 code should be passed as a three-letter string in uppercase.

### 6. Retrieve information about a country with the specified ISO 3166-1 alpha-2 code

**Endpoint:** `/country/iso2/name`

**HTTP Method:** GET

**Description:** Retrieves information about a country with the specified ISO 3166-1 alpha-2 code.

**Parameters:**

- iso2 (string): the ISO 3166-1 alpha-2 code of the country (e.g. US)

**Example Request:**

```
GET /country/iso2/ES
```

**Example Response:**

```json
{
	"data": [
		{
			"admin_name": "Madrid",
			"capital": "primary",
			"city": "Madrid",
			"city_ascii": "Madrid",
			"country": "Spain",
			"id": 89,
			"iso2": "ES",
			"iso3": "ESP",
			"lat": "40.4169",
			"lng": "-3.7033",
			"population": "6211000"
		},
		{
			"admin_name": "Catalonia",
			"capital": "admin",
			"city": "Barcelona",
			"city_ascii": "Barcelona",
			"country": "Spain",
			"id": 151,
			"iso2": "ES",
			"iso3": "ESP",
			"lat": "41.3825",
			"lng": "2.1769",
			"population": "4800000"
		},
      ...
      	],
	"page": 1,
	"total_data": 754,
	"total_pages": 8
}
```
Note: The ISO 3166-1 alpha-2 code should be passed as a two-letter string in uppercase.

### 7. Retrieve information about a city with the specified latitude and longitude

**Endpoint:** `/city/lat/<string:lat>/lng/<string:lng>`

**HTTP Method:** GET

**Description:** Retrieves information about a city with the specified latitude and longitude.

**Parameters:**

- lat (string): the latitude of the city
- lng (string): the longitude of the city

**Example Request:**

```
GET city/lat/-23.55/lng/-46.6333
```

**Example Response:**

```json
{
	"admin_name": "Sao Paulo",
	"capital": "admin",
	"city": "Sao Paulo",
	"city_ascii": "Sao Paulo",
	"country": "Brazil",
	"id": 8,
	"iso2": "BR",
	"iso3": "BRA",
	"lat": "-23.55",
	"lng": "-46.6333",
	"population": "23086000"
}
```
