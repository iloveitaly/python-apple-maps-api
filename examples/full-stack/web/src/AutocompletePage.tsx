import { useEffect, useState } from "react"

type AutocompleteResult = {
  displayLines?: string[] | null
  completionUrl?: string | null
  location?: { latitude: number; longitude: number } | null
}

export function AutocompletePage() {
  const [query, setQuery] = useState("")
  const [results, setResults] = useState<AutocompleteResult[]>([])
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const q = query.trim()
    if (!q) {
      setResults([])
      setError(null)
      setLoading(false)
      return
    }

    setLoading(true)
    const timer = setTimeout(() => {
      fetch(`/api/autocomplete?q=${encodeURIComponent(q)}`)
        .then(async (r) => {
          if (!r.ok) throw new Error(`HTTP ${r.status}`)
          return r.json()
        })
        .then((data) => {
          setResults(data.results ?? [])
          setError(null)
        })
        .catch((e) => setError(String(e)))
        .finally(() => setLoading(false))
    }, 250)

    return () => clearTimeout(timer)
  }, [query])

  return (
    <div style={{ maxWidth: 560, margin: "0 auto", padding: 16 }}>
      <h1 style={{ fontSize: 18, margin: "0 0 12px" }}>Autocomplete</h1>
      <input
        autoFocus
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder='try "1 Apple Park"'
        style={{ width: "100%", padding: "8px 10px", fontSize: 16, boxSizing: "border-box" }}
      />
      {loading && <p style={{ color: "#666" }}>searching…</p>}
      {error && <p style={{ color: "crimson" }}>{error}</p>}
      {!loading && query.trim() && results.length === 0 && !error && (
        <p style={{ color: "#666" }}>no results</p>
      )}
      <ul style={{ listStyle: "none", padding: 0, margin: "12px 0 0" }}>
        {results.map((r, i) => (
          <li
            key={i}
            style={{
              padding: "10px 0",
              borderBottom: "1px solid #eee",
            }}
          >
            <div style={{ fontWeight: 600 }}>{r.displayLines?.[0] ?? "(untitled)"}</div>
            {r.displayLines?.[1] && (
              <div style={{ color: "#555", fontSize: 14 }}>{r.displayLines[1]}</div>
            )}
            {r.location && (
              <div style={{ color: "#888", fontSize: 12, marginTop: 2 }}>
                {r.location.latitude.toFixed(5)}, {r.location.longitude.toFixed(5)}
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  )
}
