const User = require('../models/User')
const {StatusCodes} = require('http-status-codes')
const jwt = require('jsonwebtoken')
const {BadRequestError, UnauthenticatedError} = require('../errors')
const bcrypt = require('bcryptjs')

const register = async (req, res) => {
    // create user
    const user = await User.create({ ...req.body })

    // create token
    const token = jwt.sign({userId:user._id, name:user.name}, 'jwtSecret', {expiresIn:'30d',})
    res.status(StatusCodes.CREATED).json({ user:{name:user.name}, token })
}

const login = async (req, res) => {
    const {email, password} = req.body
    if (!email || !password){
        throw new BadRequestError('Please provide email and password')
    }

    // check if user exists
    const user  =  await User.findOne({email})
    if (!user){
        throw new UnauthenticatedError('Invalid credentials')
    }

    const token = jwt.sign({userId:user._id, name:user.name}, 'jwtSecret', {expiresIn:'30d',})

    // compare req.password and user.password
    const isMatch = await bcrypt.compare(password, user.password)
    if (!isMatch) {
        throw new UnauthenticatedError('Invalid credentials')
    }

    res.status(StatusCodes.OK).json({ user:{name:user.name}, token })
}

module.exports = {
    register,
    login
}