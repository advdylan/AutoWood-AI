import {defineStore} from 'pinia'
import axios from 'axios'

export const useNewProjectStoreBeta = defineStore('newproject', {
  state: () => ({

    category: [],
    worktimetype: [],
    accesorytype: [],
    accesories: [],
    wood: [],
    collection: [],
    paints: [],
    elements: [],
    boxes: [],
    boards: [],
    marginA: 0,
    marginB: 0,
    marginC: 0,
    customer: {
      name: '',
      phone_number: 0,
      street: '',
      code: '',
      city: '',
      email: ''
    },
    files: [],
    projectName: null,
    selectedWood : null,
    selectedCategory : null,
    selectedCollection :null,
    selectedPaint : null,
    selectedFile: null,
    warehouseBoards: [],
    chosenWoodType: null,
    chosenThicknesses: new Set(),
    highlightedRows: new Set(),
    creationMode: '',
    productionSteps: [],
    chosenProductionSteps: [],
    deletedIDs: [],
    paintsWarehouse: [
  {
    name: "BlackPaint",
    isActive: false,
    data: [
      { day: new Date("2023-05-01"), capacity: 32 },
      { day: new Date("2023-05-02"), capacity: 31 },
      { day: new Date("2023-05-03"), capacity: 28 },
      { day: new Date("2023-05-04"), capacity: 25 },
      { day: new Date("2023-05-05"), capacity: 22 },
      { day: new Date("2023-05-06"), capacity: 20 },
      { day: new Date("2023-05-07"), capacity: 18 },
      { day: new Date("2023-05-08"), capacity: 15 },
      { day: new Date("2023-05-09"), capacity: 12 },
      { day: new Date("2023-05-10"), capacity: 10 },
      { day: new Date("2023-05-11"), capacity: 15 },
      { day: new Date("2023-05-12"), capacity: 20 },
      { day: new Date("2023-05-13"), capacity: 25 },
      { day: new Date("2023-05-14"), capacity: 30 },
      { day: new Date("2023-05-15"), capacity: 35 },
      { day: new Date("2023-05-16"), capacity: 40 },
      { day: new Date("2023-05-17"), capacity: 45 },
      { day: new Date("2023-05-18"), capacity: 50 },
      { day: new Date("2023-05-19"), capacity: 55 },
      { day: new Date("2023-05-20"), capacity: 60 },
      { day: new Date("2023-05-21"), capacity: 65 },
      { day: new Date("2023-05-22"), capacity: 70 },
      { day: new Date("2023-05-23"), capacity: 75 },
      { day: new Date("2023-05-24"), capacity: 80 },
      { day: new Date("2023-05-25"), capacity: 85 },
      { day: new Date("2023-05-26"), capacity: 90 },
      { day: new Date("2023-05-27"), capacity: 95 },
      { day: new Date("2023-05-28"), capacity: 100 },
      { day: new Date("2023-05-29"), capacity: 95 },
      { day: new Date("2023-05-30"), capacity: 90 },
      { day: new Date("2023-05-31"), capacity: 85 }
    ]
  },
  {
    name: "WhitePaint",
    isActive: true,
    data: [
      { day: new Date("2023-05-01"), capacity: 85 },
      { day: new Date("2023-05-02"), capacity: 82 },
      { day: new Date("2023-05-03"), capacity: 79 },
      { day: new Date("2023-05-04"), capacity: 76 },
      { day: new Date("2023-05-05"), capacity: 73 },
      { day: new Date("2023-05-06"), capacity: 70 },
      { day: new Date("2023-05-07"), capacity: 67 },
      { day: new Date("2023-05-08"), capacity: 64 },
      { day: new Date("2023-05-09"), capacity: 61 },
      { day: new Date("2023-05-10"), capacity: 58 },
      { day: new Date("2023-05-11"), capacity: 55 },
      { day: new Date("2023-05-12"), capacity: 52 },
      { day: new Date("2023-05-13"), capacity: 49 },
      { day: new Date("2023-05-14"), capacity: 46 },
      { day: new Date("2023-05-15"), capacity: 43 },
      { day: new Date("2023-05-16"), capacity: 40 },
      { day: new Date("2023-05-17"), capacity: 37 },
      { day: new Date("2023-05-18"), capacity: 34 },
      { day: new Date("2023-05-19"), capacity: 31 },
      { day: new Date("2023-05-20"), capacity: 28 },
      { day: new Date("2023-05-21"), capacity: 25 },
      { day: new Date("2023-05-22"), capacity: 22 },
      { day: new Date("2023-05-23"), capacity: 19 },
      { day: new Date("2023-05-24"), capacity: 16 },
      { day: new Date("2023-05-25"), capacity: 13 },
      { day: new Date("2023-05-26"), capacity: 10 },
      { day: new Date("2023-05-27"), capacity: 7 },
      { day: new Date("2023-05-28"), capacity: 4 },
      { day: new Date("2023-05-29"), capacity: 1 },
      { day: new Date("2023-05-30"), capacity: 0 },
      { day: new Date("2023-05-31"), capacity: 5 }
    ]
  },
  {
    name: "RedPaint",
    isActive: true,
    data: [
      { day: new Date("2023-05-01"), capacity: 45 },
      { day: new Date("2023-05-02"), capacity: 48 },
      { day: new Date("2023-05-03"), capacity: 52 },
      { day: new Date("2023-05-04"), capacity: 56 },
      { day: new Date("2023-05-05"), capacity: 60 },
      { day: new Date("2023-05-06"), capacity: 64 },
      { day: new Date("2023-05-07"), capacity: 68 },
      { day: new Date("2023-05-08"), capacity: 72 },
      { day: new Date("2023-05-09"), capacity: 76 },
      { day: new Date("2023-05-10"), capacity: 80 },
      { day: new Date("2023-05-11"), capacity: 76 },
      { day: new Date("2023-05-12"), capacity: 72 },
      { day: new Date("2023-05-13"), capacity: 68 },
      { day: new Date("2023-05-14"), capacity: 64 },
      { day: new Date("2023-05-15"), capacity: 60 },
      { day: new Date("2023-05-16"), capacity: 56 },
      { day: new Date("2023-05-17"), capacity: 52 },
      { day: new Date("2023-05-18"), capacity: 48 },
      { day: new Date("2023-05-19"), capacity: 44 },
      { day: new Date("2023-05-20"), capacity: 40 },
      { day: new Date("2023-05-21"), capacity: 36 },
      { day: new Date("2023-05-22"), capacity: 32 },
      { day: new Date("2023-05-23"), capacity: 28 },
      { day: new Date("2023-05-24"), capacity: 24 },
      { day: new Date("2023-05-25"), capacity: 20 },
      { day: new Date("2023-05-26"), capacity: 16 },
      { day: new Date("2023-05-27"), capacity: 12 },
      { day: new Date("2023-05-28"), capacity: 8 },
      { day: new Date("2023-05-29"), capacity: 4 },
      { day: new Date("2023-05-30"), capacity: 0 },
      { day: new Date("2023-05-31"), capacity: 10 }
    ]
  },
  {
    name: "BluePaint",
    isActive: true,
    data: [
      { day: new Date("2023-05-01"), capacity: 10 },
      { day: new Date("2023-05-02"), capacity: 15 },
      { day: new Date("2023-05-03"), capacity: 20 },
      { day: new Date("2023-05-04"), capacity: 25 },
      { day: new Date("2023-05-05"), capacity: 30 },
      { day: new Date("2023-05-06"), capacity: 35 },
      { day: new Date("2023-05-07"), capacity: 40 },
      { day: new Date("2023-05-08"), capacity: 45 },
      { day: new Date("2023-05-09"), capacity: 50 },
      { day: new Date("2023-05-10"), capacity: 55 },
      { day: new Date("2023-05-11"), capacity: 60 },
      { day: new Date("2023-05-12"), capacity: 65 },
      { day: new Date("2023-05-13"), capacity: 70 },
      { day: new Date("2023-05-14"), capacity: 75 },
      { day: new Date("2023-05-15"), capacity: 80 },
      { day: new Date("2023-05-16"), capacity: 85 },
      { day: new Date("2023-05-17"), capacity: 90 },
      { day: new Date("2023-05-18"), capacity: 95 },
      { day: new Date("2023-05-19"), capacity: 100 },
      { day: new Date("2023-05-20"), capacity: 95 },
      { day: new Date("2023-05-21"), capacity: 90 },
      { day: new Date("2023-05-22"), capacity: 85 },
      { day: new Date("2023-05-23"), capacity: 80 },
      { day: new Date("2023-05-24"), capacity: 75 },
      { day: new Date("2023-05-25"), capacity: 70 },
      { day: new Date("2023-05-26"), capacity: 65 },
      { day: new Date("2023-05-27"), capacity: 60 },
      { day: new Date("2023-05-28"), capacity: 55 },
      { day: new Date("2023-05-29"), capacity: 50 },
      { day: new Date("2023-05-30"), capacity: 45 },
      { day: new Date("2023-05-31"), capacity: 40 }
    ]
  },
  {
    name: "YellowPaint",
    isActive: false,
    data: [
      { day: new Date("2023-05-01"), capacity: 60 },
      { day: new Date("2023-05-02"), capacity: 62 },
      { day: new Date("2023-05-03"), capacity: 64 },
      { day: new Date("2023-05-04"), capacity: 66 },
      { day: new Date("2023-05-05"), capacity: 68 },
      { day: new Date("2023-05-06"), capacity: 70 },
      { day: new Date("2023-05-07"), capacity: 72 },
      { day: new Date("2023-05-08"), capacity: 74 },
      { day: new Date("2023-05-09"), capacity: 76 },
      { day: new Date("2023-05-10"), capacity: 78 },
      { day: new Date("2023-05-11"), capacity: 80 },
      { day: new Date("2023-05-12"), capacity: 78 },
      { day: new Date("2023-05-13"), capacity: 76 },
      { day: new Date("2023-05-14"), capacity: 74 },
      { day: new Date("2023-05-15"), capacity: 72 },
      { day: new Date("2023-05-16"), capacity: 70 },
      { day: new Date("2023-05-17"), capacity: 68 },
      { day: new Date("2023-05-18"), capacity: 66 },
      { day: new Date("2023-05-19"), capacity: 64 },
      { day: new Date("2023-05-20"), capacity: 62 },
      { day: new Date("2023-05-21"), capacity: 60 },
      { day: new Date("2023-05-22"), capacity: 58 },
      { day: new Date("2023-05-23"), capacity: 56 },
      { day: new Date("2023-05-24"), capacity: 54 },
      { day: new Date("2023-05-25"), capacity: 52 },
      { day: new Date("2023-05-26"), capacity: 50 },
      { day: new Date("2023-05-27"), capacity: 48 },
      { day: new Date("2023-05-28"), capacity: 46 },
      { day: new Date("2023-05-29"), capacity: 44 },
      { day: new Date("2023-05-30"), capacity: 42 },
      { day: new Date("2023-05-31"), capacity: 40 }
    ]
  }
],
  }),

  getters: {
    filteredBoards: (state) => {
      return state.warehouseBoards.filter(
        (wood) => wood.wood_type.name === state.chosenWoodType && state.chosenThicknesses.has(wood.dimZ)
      );
    },
    accesoriesStore() {
      return this.accesories.map(accesory => ({
        ...accesory,
        sum: accesory.type.price * accesory.quantity      
      }))
    },
    pricedElements() {
      return this.elements.map(element => {
       
        
        let volume = (element.element.dimX / 1000) * (element.element.dimY / 1000) * (element.element.dimZ / 1000)
        let wood_type = this.wood.find(w => w.name === element.element.wood_type.name)
        
        if (!wood_type) {
          console.error(`Nie znaleziono typu drewna: ${element.element.wood_type}`)
          return {
            ...element,
            price: 'Nieznana cena - brak typu drewna'
          }
        }
     
        let price = (volume * wood_type.price) * element.quantity
        
        return {
          ...element,
          price: parseFloat(price).toFixed(2)
        }
          
         
      })
    },
    
    worktimeCost() {
      return this.boxes.map(works => ({
        ...works,
        sum: works.value * (works.hours * works.workers)
      })
        
      )
    }

  }, 
  actions: {

    
    setData(data){
      this.category = data.category,
      this.worktimetype = data.worktimetype,
      this.accesorytype = data.accesorytype,
      this.wood = data.wood,
      this.collection = data.collection,
      this.paints = data.paints
      this.boxes = this.worktimetype.map(item => {
        return { text: item.name, value: item.cost, checked: false, hours: 0, workers: 0}
      })
    },

    chooseWoodType(woodType) {

      console.log("Selected Wood Type:", woodType); // Logs the clicked woodType
      this.chosenWoodType = woodType.name
      console.log("Updated Chosen Wood Type:", this.chosenWoodType); // Logs updated value

    },

    highlightRow(board) {
      console.log(board)
      if (this.highlightedRows.has(board)){
        console.log("It has same row")
        this.highlightedRows.delete(board)
      }
      else {
        this.highlightedRows.add(board)
      }
      
      
    },

    $resetBoxes() {
      this.boxes = this.worktimetype.map(item => {
        return { text: item.name, value: item.cost, checked: false, hours: 0, workers: 0}
      })
    },

    setBoxesViaProps(props) {     
      this.boxes = props.map(item => {
        return { text: item.worktime.name,
            value: item.cost,
            checked: false,
            hours: item.duration,
            workers: item.workers
          }      
      })
    },


    async loadData(){
      await axios
      .get(`/api/v1/project/`)
      .then(response =>{
        //console.log(JSON.stringify(response.data))
        this.setData(response.data)      
      })
      .catch(error =>{
        console.log(error)     
      })
    },

    async loadBoards() {
     await axios
    .get(`/api/v1/warehouse/boards/`)
    .then(response =>{
        //console.log(response)
        this.warehouseBoards = response.data
    })
    .catch(error => {
        //console.log(error)
    })

    },

    async updateAccesories(editedData) {
      await axios
      .post(`/api/v1/newproject/update-accesorytype/`, editedData, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        console.log(JSON.stringify(response.data))   
        return true   
      })
      .catch(error => {
        //console.log(JSON.stringify(response.data))  
        console.log(error)
        return false
      })
    },

    async getProductionSteps() {
      await axios
      .get(`/api/v1/production/stages/`)
      .then (response => {
        console.log(JSON.stringify(response.data))
        this.productionSteps = response.data
      })
      .catch(error => {
        console.log(error)
      })
    },


    addElement(element) {   
      this.elements.push({
        element: {
          name: element.element.name,
          dimX: element.element.dimX,
          dimY: element.element.dimY,
          dimZ: element.element.dimZ,
          wood_type: element.element.wood_type
        },
        quantity: element.quantity
      });     
    },
    addBoard(board) { 
      console.log(board)  
      this.boards.push({
        board: {
          dimX: board.board.dimX,
          dimY: board.board.dimY,
          dimZ: board.board.dimZ,
          wood_type: board.board.wood_type
        },
        quantity: board.quantity
      });     
    },
    addWarehouseBoard(board) { 
      console.log(board)  
      this.warehouseBoards.push({
        
          dimX: board.board.dimX,
          dimY: board.board.dimY,
          dimZ: board.board.dimZ,
          wood_type: board.board.wood_type,
          quantity: board.quantity
      });     
    },


    deleteElement(element) {
      this.elements.pop(element)
    },
  
    addAccesory(accesory) {    
      //console.log(accesory)  
      const newAccesory = {
        id: accesory.id,
        project: 0,
        quantity: accesory.quantity,
        type: {
            description: accesory.description,
            id: accesory.id,
            name: accesory.name,
            price: accesory.price,
            type: accesory.type,
            weight: accesory.weight
        }
    }
    //console.log("NewAcc:" , newAccesory)
    this.accesories.push(newAccesory)
    },
    addThickness(thickness) {
      if (this.chosenThicknesses.has(thickness)) {
        this.chosenThicknesses.delete(thickness);
      } else {
        this.chosenThicknesses.add(thickness);
    }

    },
    addAccesorytype(accesory) {
      this.accesorytype.push(accesory)
    },

    deleteAccesory(accesory) {
      
      this.accesories.pop({
        name: accesory.name,
        price: accesory.price,
        type: accesory.type,
        quantity: accesory.quantity
      })
    },

    setElements(newElements) {
      this.elements = newElements;
    },

    setAccesories(newAccesories) {
      this.accesories = newAccesories
    },

    setWorktimes(worktimes) {
      this.boxes = worktimes
    },
    setMode(mode) {
      this.creationMode = mode
    },
    addNewStage(stage) {
      this.chosenProductionSteps.push(stage)
    },
    deleteStage(stage) {
      const stageToDelete = this.chosenProductionSteps.findIndex(item => item.stage_name === stage.stage_name & item.shortcut === stage.shortcut)
      this.chosenProductionSteps.splice(stageToDelete, 1)
    
    },
    deleteNewStage(stage) {
      const stageToDelete = this.productionSteps.findIndex(item => item.stage_name === stage.stage_name & item.shortcut === stage.shortcut)
      this.productionSteps.splice(stageToDelete, 1)
      this.deletedIDs.push(stage.id)

    },

    addProductionStages(stages) {
      //clear previous set steps
      this.chosenProductionSteps = []

      for(let stage of stages) {
          this.chosenProductionSteps.push(stage)
          console.log(`Stage: ${stage}`)
      }
  },



    $reset() {
      this.category = []
      this.worktimetype = []
      this.accesorytype = []
      this.accesories = []
      this.wood = []
      this.collection = []
      this.paints = []
      this.elements = []
      this.boxes = []
      this.marginA = 0
      this.marginB = 0
      this.marginC = 0
      this.customer = {
        name: '',
        phone_number: '',
        street: '',
        code: '',
        city: '',
        email: ''
      }
      this.files = []
      
      this.projectName = null
      this.selectedWood = null
      this.selectedCategory = null
      this.selectedCollection = null
      this.selectedPaint = null
      this.selectedFile = null
    },
  }
})