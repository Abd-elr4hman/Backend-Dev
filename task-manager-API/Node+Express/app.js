// get express
const express = require('express');

// start express app
const app = express();

// get tasks routes
const tasks = require('./routes/tasks')

// db connection func
const connectDB = require('./db/connect')

// not found middleware
const notFound = require('./middleware/notfound')

// error handler middleware
const errorHandlerMiddleware = require('./middleware/errorhandler')

//
require('dotenv').config()

const port = 3000;

//middleware
app.use(express.json())


//routes
app.get('/hello', (req,res)=>{
    res.send('task manager app')
})

app.use('/api/v1/tasks', tasks)
// app.get('api/v1/tasks')
// app.post('api/v1/tasks')
// app.get('api/v1/tasks/:id')   // get a single task
// app.patch('api/v1/tasks/:id')   // update a single task
// app.delete('api/v1/tasks/:id')   //  delete a single task


//any route not created
app.use(notFound)

// handle errors
app.use(errorHandlerMiddleware)



const start = async ()=>{
    try{
        await connectDB(process.env.MONGO_URI)
        app.listen(port, console.log(`Server is listening on ${port}`))

    } catch(error) {
        console.log(error)
    }
}

start()