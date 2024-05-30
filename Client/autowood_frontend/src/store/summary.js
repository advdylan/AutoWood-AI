import { defineStore } from 'pinia'
import { setTransitionHooks } from 'vue'

export const useSummaryStore = defineStore('summary', {
    state: () => ({
      summaryCosts: 0,
      elementsMargin: 0,
      accesoriesMargin: 0,
      additionalMargin: 0,
      summaryCostsWithMargin: 0,
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
    },
  })

  //Zastanów się czy nie warto tu przenieść wartości
  // z komponentu Summary.vue do tego store. Zrobiłeś tak ponieważ 
  // najpierw napisałeś wszystkie computed value w komponencie
  // i Ci się nie chciało tego poprawiać