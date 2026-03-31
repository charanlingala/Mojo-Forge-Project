import "./globals.css"
import type { Metadata } from "next"

export const metadata: Metadata = {
  title: "MoJoForge",
  description: "Multi-agent AI orchestration app"
}

export default function RootLayout({
  children
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}