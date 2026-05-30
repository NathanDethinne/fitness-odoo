import { Component, xml, useState, onMounted, useRef } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class MyProgress extends Component {
    static template = xml`
    <div class="dropdown">
        <select t-on-change="onSelectedExercise">
            <option t-foreach="catalog_list" t-as="exercise" t-key="exercise.id"
    `;
    setup() {
        this.state = useState({
            selectedExerciseId: null,
            chartData: [],
            catalog_list: [],
        });
        this.orm = useService("orm");
        onMounted(async () => {
            await this.loadCatalog();
        });
    }
    onSelectedExercise(event) {
        this.state.selectedExerciseId = +event.target.value;
        this.loadChartData();
    }
    async loadCatalog() {
        const exercise_catalog = await this.orm.searchRead(
            "fitness.catalog",
            [],
            ['name', 'muscle_group']
        );
        this.state.catalog_list = exercise_catalog
    }

    async loadChartData() {
        const records = await this.orm.searchRead(
            "fitness.set",
            [["exercise_id", "=", this.state.selectedExerciseId]],
            ["weight", "set_date"],
            {order: "set_date asc"}
        );
        this.state.chartData = records;
    }
}

registry.category("actions").add("display_progress", MyProgress);