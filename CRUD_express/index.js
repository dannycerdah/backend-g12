//usando ECMAScript
import express, { json } from 'express';
import cors from "cors";
//usando CommonJs
// const express = require('express')

const servidor = express();
//ahora ya podemos recibir 
servidor.use(express.json());
servidor.use(express.raw());
servidor.use(express.urlencoded({extended: true}));
//el metodo get siempre va a poder ser accedido a pesar de solo poner el post
servidor.use(cors({origin:['http://127.0.0.1'],  //'*'
                  methods : ["POST","PUT","DELETE"], //'*'
                  allowedHeaders: ["Content-Type","Authorization"], //'*'
                }));


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
    
servidor.post('/productos',(req,res)=>{
    console.log(req.body);
    const data = req.body

    productos.push(data)

    return res.status(201).json({
        message:'Producto agregado'
    })
})
    
servidor.get('/productos',(req,res)=>{
    const data = productos
    return res.json({
        data
    })
})
    
servidor
    .route('/producto/:id')
    .get((req,res)=>{
    console.log(req.params);
    const {id}= req.params
    
    
    if(productos.length < id){
        return res.status(400).json({
            message : 'El producto no existe' 
        })
    }else{
        const data = productos[id-1]

        return res.json({
            data 
        })
    }
   
})
    
    .put((req,res)=>{
    const {id}= req.params
    if(productos.length < id){
        return res.status(400).json({
            message :'El producto no existe'
        })
    }
    else{
        productos[id-1] = req.body

        return res.json({
            message :'Producto actualizado exitosamente',
            content : productos[id-1]
        })
         
    }
  
})
    .delete((req,res)=>{
        const {id} = req.params
        if(productos.length < id){
            return res.json({
                message:'Producto a eliminar no existe'
            })
        }else{
            //metodo de los arreglos para eliminar uno o mas elementos 
            //indicando la posicion y la cantidad de elementos
            productos.splice(id-1,1)
            return res.json({
                message :"Producto eliminado exitosamente"
            })
        }
    })

servidor.listen(3000,()=>{
    console.log("Servidor corriendo exitosamente en el puerto 3000")    
})
