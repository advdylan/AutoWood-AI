import {defineStore} from 'pinia'
import axios from 'axios'

export const useWarehouseStore = defineStore('WarehouseStore', {
  state: () => ({

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
    isActive: false,
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
    isActive: false,
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
    isActive: false,
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


  }, 
  actions: {

    togglePaint(paint) {
        paint.isActive =! paint.isActive
    },


  }
})