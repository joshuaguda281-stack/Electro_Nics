{
  "version"; 2,
  "builds"; [
    {
      "src": "electro_nics/wsgi.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "15mb"
      }
    }
  ],
  "routes"; [
    { "src": "/static/(.*)", "dest": "/static/$1" },
    { "src": "/(.*)", "dest": "electro_nics/wsgi.py" }
  ]
}
