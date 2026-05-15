Here is the Markdown representation of the issue:

# [refactor: replace radar / apple maps](https://github.com/iloveitaly/movie-tickets/issues/125)
**Issue #125** | **State:** Open | **Author:** [@iloveitaly](https://github.com/iloveitaly)
**Created At:** 2026-04-22T14:55:10Z | **Updated At:** 2026-05-15T17:12:21Z

---

Radar replacement:

* core needs: autocomplete API, address from lat + lng, and nice to have postal code / address => full geolocation.
* Ideally, they would have a React package with a mapping component so we could show things visually like we do for the larger map and for the location selecting on the host page. If we can't find a service that's low cost enough that provides this, we could use OpenStreetMaps or another mapping provider.
* One thing that's kind of interesting is Apple Maps actually has pretty good functionality and it's super cheap. However, the libraries for Apple Maps are basically non-existent. And you need to sign up for an Apple developer account in order to get access to Apple Maps.
* primarily US coverage, but international would be nice.
* Tried locationIQ (terrible), Radar is too expensive, MapBox seemed decently expensive, Google is really expensive, Apple maps was really cheap.

Mike's gut instinct:

* I looked at Mapbox and a couple of other solutions, and they all seemed pretty expensive. And in some cases weren't as good as radar for the geolocation stuff. Google maps is really expensive.
* We should use Apple Maps and build custom API libraries for the geocoding stuff and for React mapping components.
* What's interesting about the Apple Maps is we could build the API libraries for it and open source it, and that'd be kind of a cool thing to put out there. And with AI, it shouldn't be that much work, especially if we point the AI to how the radar maps are designed. We could just model off of a lot of their React components and props and stuff like that. 
* **The big open question is:** does Apple provide an acceptable level of API primitives that will solve our problems? Do they have geocoding, map tiles that are standardized, that kind of thing.