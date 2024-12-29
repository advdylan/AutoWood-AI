<template>
<div class="card">
  <header class="card-header">
    <p class="card-header-title"> {{ $t('cut-optimizer') }}</p>

  </header>

  <div class="card">
  <div class="card-content">
    <div class="content">
      <div class="columns">

        <div class="column is-one-third">
            <b-table :data="elements" striped narrow>
      <b-table-column label="Name">
        <template #default="props">
          <input
            type="text"
            class="input is-small"
            v-model="props.row.element.name"
          />
        </template>
      </b-table-column>

      <b-table-column label="X">
        <template #default="props">
          <input
            
            class="input is-small"
            v-model.number="props.row.element.dimX"
          />
        </template>
      </b-table-column>

      <b-table-column label="Y">
        <template #default="props">
          <input
            
            class="input is-small"
            v-model.number="props.row.element.dimY"
          />
        </template>
      </b-table-column>

      <b-table-column label="Z">
        <template #default="props">
          <input
            
            class="input is-small"
            v-model.number="props.row.element.dimZ"
          />
        </template>
      </b-table-column>

      <b-table-column label="Wood">
        <template #default="props">
          <input
            
            class="input is-small"
            v-model="props.row.element.wood_type"
          />
        </template>
      </b-table-column>

      <b-table-column label="Quantity">
        <template #default="props">
          <input
            
            class="input is-small"
            v-model.number="props.row.quantity"
          />
        </template>
      </b-table-column>
      
      <b-table-column label="Actions">
        <template #default="props">
          <button
            class="button is-small is-danger"
            @click="removeFormat(props.index)"
          >
            Remove
          </button>
        </template>
      </b-table-column>
    </b-table>
    
        </div>

        <div class="column">
            
        </div>

        




      </div>
    </div>
  </div>
</div>
</div>


</template>














<script setup>


let elements = [
      ]
</script>
<style lang="scss">
.content table td {
    padding: 0.1em 0.1em;
}
</style>