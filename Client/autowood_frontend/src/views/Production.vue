<template>

<div class="card">


    <div class="card">
        <div class="card-content">
            <div class="columns">
                <div class="column is-full">
                    <div class="label has-text-centered is-size-5"> {{ $t('production') }}</div>
                    <div class="box">
                        
                        
                    </div>

                </div>
            </div>

   
</div>
    </div>
        </div>



</template>

<script setup>


const productionDataSet = [
    {project: {},
     productionStages: 'array of stages(PTNSO)',
     status: 'status (Cut, CNC, granding, painting, packaging )',
     dateOfOrder: 'dateofOrder',
     dateOfDelivery: 'dateOfDelivery',
    }
]

</script>

<style lang="css" scoped>

</style>