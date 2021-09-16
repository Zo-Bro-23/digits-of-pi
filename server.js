const express = require('express')
const app = express()
app.use(express.static('.'))
app.get('/', (req, resp) => {
    resp.sendFile('index.html', {root: __dirname})
})

app.listen(5210)