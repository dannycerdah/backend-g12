//usando ECMAScript
import express from 'express';
//usando CommonJs
// const express = require('express')

const servidor = express()
//ahora ya podemos recibir 
servidor.use(express.json())
servidor.use(express.raw())
servidor.use(express.urlencoded({extended: true}))


const productos = [
    {
        nombre: 'platano',
        precio: 1.80,
        disponible: true
    }
]

servidor.get('/',(req,res)=>{
    return res.status(200).json({
        message:'Bienvenido a mi API de productos'
    })
})

servidor.post('/crear-producto',(req,res)=>{
    console.log(req.body);

    return res.status(201).json({
        message:'Producto agregado'
    })
})

servidor.listen(3000,()=>{
    console.log("Servidor corriendo exitosamente en el puerto 3000")    
})
