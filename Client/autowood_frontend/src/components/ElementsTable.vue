<template>
  <div class="elements-table-container">
      <table class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>Name</th>
            <th>Długość</th>
            <th>Wysokość</th>
            <th>Grubość</th>
            <th>Materiał</th>
            <th>Ilość</th>
            <th>Usuń</th>
            
          </tr>

        </thead>
        
        <tfoot>
          
          <tr>
            
          </tr>
        
        
        </tfoot>
        <tbody>
          <tr v-for="element in elements" :key="element.name">
            
            <th>{{ element.element.name }}</th>
            <td>{{ element.element.dimX }}</td>
            <td>{{ element.element.dimY }}</td>
            <td>{{ element.element.dimZ }}</td>
            <td>{{ element.element.wood_type.name }}</td>
            <td>{{ element.quantity }}</td>
            <td><b-button type="is-danger"><i class="fa-solid fa-xmark"></i></b-button></td>
          </tr>
        </tbody>
        
      </table>
    </div>
    
</template>

<script>
export default {
  name: 'ElementsTable',
  props: {
    elements: {
      type: Array,
      required: true
    }
  }
}
</script>



