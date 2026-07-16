import { useEffect, useState } from "react"
import { Map, Marker } from "mapkit-react"

// same coords reverse_geocode uses in app/main.py
const APPLE_PARK = { latitude: 37.334859, longitude: -122.0090403 }

export default function App() {
  const [token, setToken] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch("/api/maps-token")
      .then((r) => r.json())
      .then((data) => setToken(data.token))
      .catch((e) => setError(String(e)))
  }, [])

  if (error) return <p style={{ padding: 16 }}>token error: {error}</p>
  if (!token) return <p style={{ padding: 16 }}>loading map…</p>

  return (
    <div style={{ height: "100vh" }}>
      <Map
        token={token}
        initialRegion={{
          centerLatitude: APPLE_PARK.latitude,
          centerLongitude: APPLE_PARK.longitude,
          latitudeDelta: 0.01,
          longitudeDelta: 0.01,
        }}
      >
        <Marker {...APPLE_PARK} title="Apple Park" />
      </Map>
    </div>
  )
}
