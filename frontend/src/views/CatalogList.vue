<template>
    <div class="columns">
        <div class="column is-10 is-offset-1">
    <div class="projects-list-container">
        
        <b-table :data="catalog_product_data">
            <div class="box">
            <div class="label has-text-centered is-size-4">{{ $t("catalog_list")}}</div>
            </div>
            <template v-for="column in columns" :key="column.id">
                <b-table-column v-bind="column">
                    <template v-if="column.searchable && !column.numeric" #searchable="props">
                        <b-input
                            v-model="props.filters[props.column.field]"
                            :placeholder="$t('search')"
                            icon="magnify"/>
                    </template>
                    <template v-slot="props">
                        
                        <template v-if="column.field === 'nawigacja'">
                            <router-link :to="{ name: 'CatalogProductDetail', params: { id: props.row.id } }">
                                <b-button icon-right="circle-info">{{$t("details")}}</b-button>                               
                            </router-link>

                            <b-button 
                            @click="toggleAddToProduction = !toggleAddToProduction, setChosenProduct(props.row)"
                             icon-right="add">{{ $t("production") }}
                            </b-button>

                            <b-button @mouseenter="hoveredProjectId = props.row.id"
                             @mouseleave="hoveredProjectId = null" 
                             @click="$emit('getElements', props.row.id)" 
                             :value=props.row.id 
                             v-if="searchModal" 
                             icon-right="file-arrow-down"
                             >{{ $t("get_elements") }}
                            </b-button>
                            
                            <teleport to="body">
                            <div 
                            v-if="hoveredProjectId === props.row.id" 
                            class="notification is-info elements-list" 
                            >
                            <ul>
                                <li v-for="element in props.row.elements" :key="element.id">
                                X: {{ element.element.dimX }} Y: {{ element.element.dimY }} Z: {{ element.element.dimZ }} {{ $t("quantity") }}: {{ element.quantity }}
                                </li>
                            </ul>
                            </div>
                            </teleport>

                        </template>
                        <template v-else>
                        {{ props.row[column.field] }}
                    </template>
                    
                </template>
                </b-table-column>
            </template>
        </b-table>
    </div>
    </div>
    </div>



    <div v-bind:class="{'is-active': toggleAddToProduction}" class="modal">
        <div class="modal-background"></div>
        <div class="modal-card" style="height: 90%;
                                       width: 70%;">
          <header class="modal-card-head">
            <p class="modal-card-title">{{$t('add_to_production')}}</p>
            <button @click="toggleAddToProduction = !toggleAddToProduction" class="delete" aria-label="close"></button>
          </header>
          <section class="modal-card-body has-text-centered">

           <div class="card-content">
            <div class="columns">
                                <div class="column">
                                  <div class="box">
                                    <div class="label is-size-5">Dodajesz do produkcji </div>
                                    <nav class="level is-centered">
                                        <div class="level-item has-text-centered">
                                            <div class="level-item">
                                                <div v-if="chosenProduct" class="section">
                                                    <div class="label">ID</div>
                                                    <div class="box">
                                                        {{ chosenProduct.id }}
                                                    </div>
                                                </div>

                                                <div v-if="chosenProduct" class="section">
                                                    <div class="label">Name</div>
                                                    <div class="box">
                                                        {{ chosenProduct.name }}
                                                    </div>
                                                </div>

                                                <div v-if="chosenProduct" class="section">
                                                    <div class="label">Category</div>
                                                    <div class="box">
                                                        {{ chosenProduct.category }}
                                                    </div>
                                                </div>

                                                <div v-if="chosenProduct" class="section">
                                                    <div class="label">Collection</div>
                                                    <div class="box">
                                                        {{ chosenProduct.collection }}
                                                    </div>
                                                </div>

                                                <div v-if="chosenProduct" class="section">
                                                    <div class="label">Paints</div>
                                                    <div class="box">
                                                        {{ chosenProduct.paints }}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </nav>
                                  </div>
                                </div>
                              </div>
            
            <div class="columns" >
                <div class="column is-one-quarter">
                <div class="box">
                
                    <div class="label"> {{ $t('ordered_date') }}</div>
                    <div class="box has-text-centered"> 
                        <VueDatePicker 
                            v-model="dateOrdered"
                            :enable-time-picker="false"
                            :menu-class="'datepicker-menu'"
                        />
                    </div>
                
         
                    <div class="label"> {{ $t('delivery_date') }}</div>
                    <div class="box has-text-centered"> 
                        <VueDatePicker 
                            v-model="dateOfDelivery"
                            :enable-time-picker="false"
                            :menu-class="'datepicker-menu'"
                        />
      
                </div>
                    <div class="label"> {{ $t('notes') }}</div>
                    <textarea v-model="notes" class="textarea" :placeholder="$t('notes')"></textarea>
                </div>
            </div>
            <div class="column is-one-quarter ">
            <div class="box" >  

                    <label class="label is-size-6">{{$t("client_name")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.name" class="input is-small" type="text" :placeholder="$t('client_name')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-user"></i>
                        </span>
                </p>

                <label class="label is-size-6">{{$t("number")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.phone_number" class="input is-small" type="number" :placeholder="$t('number')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-phone"></i>
                        </span>
                </p>

                <label class="label is-size-6">{{$t("street")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.street" class="input is-small" type="text" :placeholder="$t('street')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-signs-post"></i>
                        </span>
                </p>

                <label class="label is-size-6">{{$t("zip_code")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.code"  class="input is-small" type="text" :placeholder="$t('zip_code')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-map"></i>
                        </span>
                </p>

                <label class="label is-size-6">{{$t("city")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.city" class="input is-small" type="text" :placeholder="$t('city')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-house"></i>
                        </span>
                </p>

                <label class="label is-size-6">{{$t("e-mail")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.email" class="input is-small" type="text" :placeholder="$t('e-mail')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-envelope"></i>
                        </span>
                </p>
                  </div>  
                </div>
                <div class="column">
                    <div class="card">
                          <header class="card-header">
                            <p class="card-header-title is-centered is-size-4">{{$t("production_steps")}} &nbsp;<i class="fa-solid fa-list-check"></i></p>  
                          </header>
                          <production-stages></production-stages>
                          </div>
                </div>
                
                
            </div>
            <div class="box">
            <div class="buttons">
                    <div  class="button is-success" @click="parseOrderData(chosenProductId)"
                    > {{ $t('save') }} </div>
                    <div @click="toggleAddToProduction = !toggleAddToProduction" class="button is-danger"> {{ $t('cancel') }}</div>

                </div>
            </div>
        </div>
          </section>

          <footer class="modal-card-foot">
            <div class="buttons">
            </div>
          </footer>
        </div>
      </div>
    
</template>

<script setup>
import { useProjectsListStore } from '@/store/projectslist'
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'
import { BaseTransitionPropsValidators, onMounted, ref} from 'vue'
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { isValidDate } from '@/validators/Validators';
import { toast } from 'bulma-toast';
import ProductionStages from '@/components/NewProjectComponents/ProductionStages.vue';


const router = useRouter()
const ProjectsListStore = useProjectsListStore()
const newProjectStore = useNewProjectStoreBeta()
const {addProductionStages} = newProjectStore
const {chosenProductionSteps} = storeToRefs(newProjectStore)
const { loadCatalog, loadDetailProject, addNewProjectToProduction, addCatalogProductToProduction } = ProjectsListStore
const { projectlist, catalog_product,  catalog_product_data, columns,} = storeToRefs(ProjectsListStore)


const hoveredProjectId = ref(null)
const toggleAddToProduction = ref(false)
const chosenProductId = ref(null)
const chosenProduct = ref(null)
const dateOrdered = ref(null)
const dateOfDelivery = ref(null)
const notes = ref('')
const customer = ref({
        name: '',
        phone_number: 0,
        street: '',
        code: '',
        city: '',
        email: ''
})





const propsList =  defineProps({
    searchModal: Boolean,
    default: false
})





function setChosenProduct(row) {
    chosenProductId.value = row.id
    chosenProduct.value = row
    getChosenProductData()
}

function getChosenProductData() {
    if (chosenProductId) {
        console.log(chosenProductId.value)
        let order = catalog_product_data.value.find((order) => order.id = chosenProductId.value)
        console.log(order.production_stages)
        addProductionStages(order.production_stages)
    }
    else {
        console.warn(`ChosenProductID of${chosenProductId.value} doesnt exist`)

    }

}

const errors = ref([])

function parseOrderData(id) {

    console.log(`Chosen production steps: ${chosenProductionSteps}`)

    let data = {
        id: id,
        contentType: "CatalogProduct",
        dataOrdered: dateOrdered.value,
        dateOfDelivery: dateOfDelivery.value,
        notes: notes.value,
        customer: customer.value,
        productionSteps: chosenProductionSteps.value
    }

    if (!isValidDate(data.dataOrdered)) {
        errors.value.push("Invalid input of order date")
    }
    if (!isValidDate(data.dateOfDelivery)) {
        errors.value.push("Invalid input of delivery date")
    }

    
    if (!errors.value.length) {
        addCatalogProductToProduction(data)
        toast({
            message: `${data.contentType} of ID: ${data.id} Name: ${chosenProduct.value.name} added to `,
            duration: 5000,
            position: "top-center",
            type: 'is-success',
            animate: { in: 'backInDown', out: 'backOutUp' },
        })
        toggleAddToProduction.value = !toggleAddToProduction.value
        router.push('/production')
        

    }

    else {
        let msg = ''

          for (let i=0; i <errors.value.length; i++){
            msg += errors.value[i] += "\n"
          }
          toast({
              message: msg,
              duration: 5000,
              position: "top-center",
              type: 'is-danger',
              animate: { in: 'backInDown', out: 'backOutUp' },
            })

            errors.value = []
        
    }
    
}


onMounted(() => {
    if(!catalog_product.value) {
         console.log("Loading catalog")
         loadCatalog()
    }
})


</script>
<style>
.elements-list {
  position: fixed; /* Position relative to the viewport */
  width: 50%;
  top: 10%; /* Adjust based on desired position */
  left: 50%; /* Adjust based on desired position */
  transform: translate(-50%, 0); /* Center horizontally */
  z-index: 1000; /* Ensure it's on top */
  background-color: #209cee; /* Bulma's info color */
  color: white; /* Text color for better visibility */
  padding: 1rem; /* Add padding for aesthetics */
  border-radius: 5px; /* Optional: round corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add a shadow for a floating effect */
}
</style>