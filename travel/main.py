from travel import create_app


app = create_app()
# by setting debug=True we set a watch and detects changes so we don't need to refresh browser
# note that it doesn't always watch properly
# app.run(debug=True) turned off for flask debug using VS code
app.run(debug=True)
