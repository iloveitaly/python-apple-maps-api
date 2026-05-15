import { AppleMap } from "./components/AppleMap"

export default function App() {
  return (
    <div className="flex h-screen flex-col">
      <header className="flex items-center gap-2 bg-black px-4 py-3 text-white">
        <svg width="20" height="20" viewBox="0 0 814 1000" fill="currentColor">
          <path d="M788.1 340.9c-5.8 4.5-108.2 62.2-108.2 190.5 0 148.4 130.3 200.9 134.2 202.2-.6 3.2-20.7 71.9-68.7 141.9-42.8 61.6-87.5 123.1-155.5 123.1s-85.5-39.5-164-39.5c-76 0-103.7 40.8-165.9 40.8s-105-37.5-155.5-127.4C46 790.7 0 681.4 0 575.4C0 411.5 109.2 310.4 216.7 310.4c62.6 0 114.6 43.2 153.7 43.2 37.6 0 97.2-46 170.6-46 27.5 0 108.2 2.6 168.5 82.3z" />
          <path d="M554.1 88.4C584.3 51.2 605 0 605 0c0 0-57.9 2.6-120.1 32.8-35.2 16.6-87 47.5-116.9 87-26.4 34.7-49.3 94.7-49.3 153.6 0 7.1 1.3 14.2 1.9 16.5 3.2.6 8.4 1.3 13.5 1.3 55.3 0 117.5-29.5 154.9-72.6z" />
        </svg>
        <span className="font-medium">Maps Test</span>
      </header>
      <div className="flex-1">
        <AppleMap />
      </div>
    </div>
  )
}
