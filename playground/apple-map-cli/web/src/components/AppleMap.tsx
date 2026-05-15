import { useEffect, useState } from "react"
import { Map, Marker } from "mapkit-react"

const PINS = [
  {
    latitude: 37.334859,
    longitude: -122.0090403,
    title: "Apple Park",
    subtitle: "1 Apple Park Way, Cupertino, CA",
    color: "#1d1d1f",
  },
  {
    latitude: 37.3328102,
    longitude: -122.0053893,
    title: "Apple Park Visitor Center",
    subtitle: "10600 N Tantau Ave, Cupertino, CA",
    color: "#0071e3",
  },
]

const INITIAL_REGION = {
  centerLatitude: 37.3338,
  centerLongitude: -122.0072,
  latitudeDelta: 0.012,
  longitudeDelta: 0.016,
}

export function AppleMap() {
  const [token, setToken] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch("/api/maps-token")
      .then((r) => r.json())
      .then(({ token }: { token: string }) => setToken(token))
      .catch((e) => setError(String(e)))
  }, [])

  if (error) {
    return (
      <div className="flex h-full items-center justify-center text-red-500">
        Failed to load map token: {error}
      </div>
    )
  }

  if (!token) {
    return (
      <div className="flex h-full items-center justify-center text-gray-400">
        Loading map…
      </div>
    )
  }

  return (
    <div className="h-full w-full">
      <Map token={token} initialRegion={INITIAL_REGION}>
        {PINS.map((pin) => (
          <Marker
            key={pin.title}
            latitude={pin.latitude}
            longitude={pin.longitude}
            title={pin.title}
            subtitle={pin.subtitle}
            color={pin.color}
            calloutContent={
              <div className="min-w-40 p-2">
                <p className="font-semibold">{pin.title}</p>
                <p className="mt-0.5 text-sm text-gray-500">{pin.subtitle}</p>
                <p className="mt-1 text-xs text-gray-400">
                  {pin.latitude.toFixed(6)}, {pin.longitude.toFixed(6)}
                </p>
              </div>
            }
          />
        ))}
      </Map>
    </div>
  )
}
