const router = require("express").Router();
const { PythonShell } =require('python-shell');

router.post("/", (req, res, next) => {
    try {
        const { env, isFood, isDrink, time, order } = req.query;
        let args = [`${env}`, `${isFood}`, `${isDrink}`, `${time}`, `${order}`];
        PythonShell.run('order.py', { args }, (err, result) => res.status(200).json(result) );
    } catch {
        (error) => next(`Error running script: ${error}`);
    }
});

module.exports = router;