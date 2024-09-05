import { defineStore } from 'pinia'
import { setTransitionHooks } from 'vue'

export const usePricesSetup = defineStore('pricessetup', {
    state: () => ({

      newWorktimeCost: []
      
    }),
    actions: {

      updateWorktimetypes(value) {
        this.newWorktimeCost = value
      },
      async updateWorktimetypes(editedData) {
        try {
            const response = await axios.patch(`/api/v1/newproject/update-worktimetypes/`, editedData, {
                headers: {
                    'Content-Type': 'application/json',                    
                },
            });
            //console.log('Server response:', response);
            //console.log('Project updated successfully:', response.data);
        } catch (error) {
            console.error('Error updating the project:', error);
        }
    },


      

    },
  })

