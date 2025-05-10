<template>
  <div class="box">
    <div class="columns">
      <div class="column has-text-centered is-one-third">
        <div class="box">
          <div class="label has-text is-size-6">{{$t('wastes')}}</div>
          <div class="table-container">
            <table class="table is-bordered is-hoverable excel-table">
              <thead>
                <tr>
                  <th>X</th>
                  <th>Y</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(board, rowIndex) in freeBoards" :key="rowIndex">
                  <td
                    v-for="(value, colIndex) in [board.X.toFixed(2), board.Y.toFixed(2)]"
                    :key="colIndex"
                    :class="{
                      'is-selected': selectedCell.row === rowIndex && selectedCell.col === colIndex
                    }"
                    @click="selectCell(rowIndex, colIndex)"
                  >
                    {{ value  }} mm
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { computed, ref } from 'vue'

const props = defineProps({
  freeBoards: Array,
  default: () => [],
  required: true
})

const selectedCell = ref({
  row: null,
  col: null
})

function selectCell(row,col) {
  selectedCell.value = {row, col}
}

</script>


<style scoped>
.excel-table td {
  text-align: center;
  vertical-align: middle;
  cursor: pointer;
  border: 1px solid #dcdcdc;
  padding: 0.5rem;
}

.excel-table th {
  background-color: #f5f5f5;
  text-align: center;
}

.excel-table td:hover {
  background-color: #cae4fb;
}
.excel-table .is-selected {
  background-color: #b3d4fc;
  color: #000;
  font-weight: bold;
  
}

</style>