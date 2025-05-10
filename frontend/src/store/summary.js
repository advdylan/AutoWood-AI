import { defineStore } from 'pinia'


export const useSummaryStore = defineStore('summary', {
    state: () => ({
      summaryCosts: 0,
      elementsMargin: 0,
      accesoriesMargin: 0,
      additionalMargin: 0,
      summaryCostsWithMargin: 0,
      elementsCost: 0,
      accesoriesCost: 0,
      worktimeCost: 0
    }),
    actions: {
      setSummaryCosts(value) {
        this.summaryCosts = value
      },
      setElementsMargin(value) {
        this.elementsMargin = value
      },
      setAccesoriesMargin(value) {
        this.accesoriesMargin = value
      },
      setAdditionalMargin(value) {
        this.additionalMargin = value
      },
      calculateSummaryCostsWithMargin(value) {
        this.summaryCostsWithMargin = value      
      },
      setElementsCost(value) {
        this.elementsCost = value
      },
      setAccesoriesCost(value) {
        this.accesoriesCost = value
      },
      setWorktimeCost(value) {
        this.worktimeCost = value
      }

    },
  })

  //Zastanów się czy nie warto tu przenieść wartości
  // z komponentu Summary.vue do tego store. Zrobiłeś tak ponieważ 
  // najpierw napisałeś wszystkie computed value w komponencie
  // i Ci się nie chciało tego poprawiać