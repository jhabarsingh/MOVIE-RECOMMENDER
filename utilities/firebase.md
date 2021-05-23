# Deploy on Firebase
1. created firebase.json
`
{
  "hosting": {
    "public": "./dist"
  }
}
`

If using History Mode

`
{
  "hosting": {
    "public": "./dist",
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
`

2. run `firebase deploy`
