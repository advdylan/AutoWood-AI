<template>
  <ClientData v-if="detail_project"
  :customer-props = "detail_project.customer"
  :documents-props = "detail_project.document"
  :detail-project = "detail_project"
  @update:detailProject="detail_project = $event"
  >
  </ClientData>
  
  

  <div class="card">
    <header class="card-header">
      <p v-if="detail_project" class="card-header-title is-centered is-size-4">{{ $t('estimate_order') }} "{{ detail_project.name}}"</p>
    </header>
    <div class="card-content">
      <div class="columns">

        <div class="column is-half">
          <div class="card">
            <div class="card-header">
              <p class="card-header-title is-size-5">{{ $t('navigation') }}</p>
            </div>
              <div class="card-content">

                <div class="buttons">
                  <b-button @click="submitUpdateForm" type="is-success" >
                    <i class="fa-solid fa-floppy-disk"></i>
                    {{ $t('save') }}
                  </b-button>

                  <b-button type="is-danger" >
                    <i class="fa-solid fa-trash"></i>
                    {{ $t('delete') }}                  </b-button>
                  <b-button @click="downloadPriceReport(id)" class="button is-info"><i class="fa-regular fa-file">&nbsp;</i>{{$t("download_pricing_report")}}</b-button>
                  <b-button @click="downloadElementsTable(id)"  class="button is-info"><i class="fa-regular fa-file">&nbsp;</i>{{$t("download_elements_list")}}</b-button>
                  <button @click="showEditModal = true" data-target="newelement-modal" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>{{$t("edit_margin")}}</button>
                  </div>   
            </div>           
          </div>
        </div>
        

        <div class="column">
          <div class="card">
            <header class="card-header" @click="isCollapsedelements = !isCollapsedelements">
              <p class="card-header-title is-size-5">
                {{ $t('elements_list') }}
              </p>
            </header>
          <div class="card-content">
          <ElementsTable v-if="detail_project"  :elements="detail_project.elements"></ElementsTable>
          </div>

          <div class="buttons">
            <button class="button is-dark" @click="showElementModal = true" data-target="newelement-modal"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj tabelę</button>
        
          </div>
          
          </div>



          <hr class="dashed">

          <div class="card">
            <header class="card-header">
              <p class="card-header-title is-size-5">
                {{$t("accessories")}}
              </p>
            </header>


            
          <div class="card-content">
          <div class="container-cost">
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
              <thead>
                <tr>
                  <th>{{$t("name")}}</th>
                  <th>{{$t("type")}}</th>
                  <th>{{$t("weight")}}</th>
                  <th>{{$t("price")}}</th>
                  
                </tr>
              </thead>
              <tfoot>   
                <tr>       
                </tr>

              </tfoot>
              <tbody>
                
                <tr v-if="detail_project" v-for="akc in detail_project.accessories">
  
                  <th>{{ akc.type.name }}</th>
                  <td>{{ akc.type.type }}</td>
                  <td>{{ akc.type.weight }}</td>
                  <td>{{ akc.type.price }}</td>

                </tr>
                
              </tbody>
              
            </table>
            <button @click="showAccModal = true" data-target="newelement-modal" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>{{$t("edit_accessories")}}</button>
        </div>
      </div>
      </div>

      







        <div v-bind:class="{'is-active': showAccModal}" id="newelement-modal" class="modal">
          <div class="modal-background"></div>
          <div class="modal-content">
      
            <div class="modal-card">
              <header class="modal-card-head">
                    <p class="modal-card-title is-centered is-size-3">{{$t("accessories")}}</p>
                    <button class="delete" aria-label="close" @click="showAccModal = false"></button>        
                  </header>
                  <section class="modal-card-body">
                    <AccesoryProgressTable v-if="detail_project" :accesories="detail_project.accessories" addAccDetail="one"  />
                  </section>
          </div>
          </div>
        </div>
        </div>

        
    
    </div>
</div>
</div>





<div v-bind:class="{'is-active': showElementModal}" id="newelement-modal" class="modal">
  <div class="modal-background"></div>
  <div class="modal-content">


    <div class="modal-card">
      <header class="modal-card-head">
            <p class="modal-card-title is-centered is-size-3">{{$t("add_element")}}</p>
            <button class="delete" aria-label="close" @click="showElementModal = false"></button>        
          </header>
          
      
      <section class="modal-card-body">
        <div class="columns">
          <div class="column is-two-fifths">

        <form @submit.prevent="submitForm">

        <div class="field">
          <label class="label">{{$t("name")}}</label>
          <div class="control">
            <input class="input" type="text" placeholder="Nazwa" v-model="newElement.element.name">             
          </div>
        </div>

        <div class="field">
          <label class="label">{{$t("length")}}</label>
          <div class="control">
            <input class="input" type="number" placeholder="Długość" v-model="newElement.element.dimX">           
          </div>
        </div>

        <div class="field">
          <label class="label">{{$t("width")}}</label>
          <div class="control">
            <input class="input" type="number" placeholder="Szerokosć" v-model="newElement.element.dimY" >             
          </div>
        </div>

        <div class="field">
          <label class="label">{{$t("thickness")}}</label>
          <div class="control">
            <input class="input" type="number" placeholder="Grubość" v-model="newElement.element.dimZ">             
          </div>
        </div>

        <div class="field">
          <label class="label">{{$t("quantity")}}</label>
          <div class="control">
            <input class="input" type="number" placeholder="Ilość" v-model="newElement.quantity" >             
          </div>
        </div>

        <div class="field">
          <label class="label">{{$t("wood_type")}}</label>
          <div class="control">
            <div class="select">
              <select v-model="newElement.element.wood_type">
                <option v-for="woodItem in wood" :key="woodItem.id" :value="woodItem">
                  {{ woodItem.name }}
                </option>
              </select>
            </div>
          </div>
        </div>

      <footer class="modal-card-foot">
        <div class="buttons">
          <button type="submit" class="button is-success">{{$t("add_element")}}</button>
         
        </div>
      </footer>
      

    </form>
  </div>
  <div class="column">
    <ElementsTable v-if="detail_project" :elements="detail_project.elements" />
  </div>
  </div>

  </section>

  </div>
  </div>


</div>

<div v-bind:class="{'is-active': showEditModal}" id="newelement-modal" class="modal">
  <div class="modal-background"></div>
  <div class="modal-content">

    <div class="modal-card">
      <header class="modal-card-head">
            <p class="modal-card-title is-centered is-size-3">{{$t("margins")}}</p>
            <button class="delete" aria-label="close" @click="showEditModal = false"></button>        
          </header>
          <section class="modal-card-body">
            <Summary v-if="detail_project" 
            :propMarginA="Number(parseFloat(detail_project.percent_elements_margin).toFixed(2))"
            :propMarginB="Number(parseFloat(detail_project.percent_accesories_margin).toFixed(2))"
            :propMarginC="Number(parseFloat(detail_project.percent_additional_margin).toFixed(2))"
            :propElements="detail_project.elements"
            :propAccesories="detail_project.accessories"
            :propWorktimecosts="detail_project.worktimes" >
  
            </Summary>
          </section>
          
      
  </div>
  </div>


</div>
   
    
</template>
  
  <script>
  export default {
    name: 'NewProjectDetail'
  }
  
  </script>
  
  <script setup>
  import { useNewProjectStoreBeta } from '@/store/newproject'
  import { useProjectsListStore } from '@/store/projectslist'
  import { useSummaryStore } from '@/store/summary'
  import { storeToRefs } from 'pinia'
  import { ref, watchEffect, onUnmounted, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import ElementsTable from '@/components/ElementsTable'
  import AccesoryProgressTable from '@/components/NewProjectComponents/AccesoryProgressTable.vue'
  import ClientData from '@/components/NewProjectComponents/ClientData.vue'
  import Summary from '@/components/Summary.vue'

  const projectName = ref()
  const selectedWood = ref()
  const selectedCategory = ref()
  const selectedCollection = ref()
  const selectedPaint = ref()
  const showElementModal = ref(false)
  const showAccModal = ref(false)
  const showEditModal = ref(false)

  const newElement = ref({
  element: {
    name: 'Przód',
    dimX: 2500,
    dimY: 250,
    dimZ: 25,
    wood_type: ''
  },
  quantity: 1
})

  const route = useRoute()
  const id = route.params.id
  
  const ProjectsListStore = useProjectsListStore()
  const elementStore = useNewProjectStoreBeta()
  const summaryStore = useSummaryStore()


  const { loadDetailProject, updateProject, addElement, downloadElementsTable, downloadPriceReport, } = ProjectsListStore
  const {elementsCost, accesoriesCost, worktimeCost , elementsMargin, accesoriesMargin, additionalMargin,summaryCostsWithMargin,summaryCosts} = storeToRefs(summaryStore)

  const {loadData, $reset } = elementStore
 


  const {detail_project} = storeToRefs(ProjectsListStore)
  const {elements, wood, collection, paints, category, boxes, accesories, marginA, marginB, marginC} = storeToRefs(elementStore)

  async function loadAndSetProjectDetails(id) {
  try {

    await loadDetailProject(id);
    if (!detail_project.value) return;
    
    projectName.value = detail_project.value.name
    selectedWood.value = detail_project.value.wood.name
    selectedCategory.value = detail_project.value.category.name
    selectedCollection.value = detail_project.value.collection.name
    selectedPaint.value = detail_project.value.paints.name
  } catch (error) {
    console.error('Failed to load project details:', error);
  
  }
}



const submitForm = () => {
  addElement(newElement.value);
  newElement.value = {
    element: {
      name: '',
      dimX: 0,
      dimY: 0,
      dimZ: 0,
      wood_type: ''
    },
    quantity: 0
  };
};


  async function submitUpdateForm() {
        const formData = {

          id: id,
          name: detail_project.value.name,
          category: detail_project.value.category.name,
          wood: detail_project.value.wood.name,
          collection: detail_project.value.collection.name,
          paints: detail_project.value.paints.name,
          elements_margin: elementsMargin.value,
          accesories_margin: accesoriesMargin.value,
          additional_margin: additionalMargin.value,
          summary_with_margin: summaryCostsWithMargin.value,
          summary_without_margin: summaryCosts.value,
          elements: detail_project.value.elements,
          worktime: boxes.value,
          accessories: detail_project.value.accessories,
          percent_elements_margin: parseInt(marginA.value),
          percent_accesories_margin: parseInt(marginB.value),
          percent_additional_margin: parseInt(marginC.value),
          elements_cost: elementsCost.value,
          accesories_cost: accesoriesCost.value,
          worktime_cost: worktimeCost.value
          
          
  }

  console.log('Form Data before sending:', formData)                 
  updateProject(id, formData)
              }


              
  onMounted(() => {
    loadData()
    loadAndSetProjectDetails(id)
  })    
  
  
  onUnmounted(()=> {
    console.log("Unmount the NewProjectDetail")
    detail_project.value = null
    $reset()
  })

  

</script>


  
  
  
  