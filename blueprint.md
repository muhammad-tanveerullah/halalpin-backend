# HalalPin Backend Blueprint

## Overview
MVP backend for Halal discovery, listing, and vendor claim platform using Django 5.0 + DRF + PostgreSQL + PostGIS. Focus launch: Hyderabad city, scalable nationwide.

## Architecture
- **Framework**: Django 5.0 + DRF
- **Database**: PostgreSQL + PostGIS (geolocation)
- **API**: RESTful JSON, public endpoints for vendor data, user login, search, vendor claim
- **Core modules**:
  - User (auth, JWT, profile)
  - Vendor (listing, geotagged, bulk import)
  - Claim flow (free/premium)
  - Search/filter
  - Admin/management
- **Deployment**: DigitalOcean/Railway, Docker Compose

## Key MVP Decisions
- Only Hyderabad for launch
- Pre-populate from Google Maps
- Freemium and commission model
- Exclude Scholar Council, events, matrimony for MVP phase