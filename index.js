const app = require("./server");
const { config } = require('dotenv');
config();

const port = process.env.PORT || 8000;
app.listen(port, () => console.log(`Server listening on port ${port}`));