/** @odoo-module **/
import { Component , useState, onWillStart, onMounted, onWillUnmount, useRef } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { loadJS } from "@web/core/assets";

class MyProgress extends Component {
    static template = 'fitness_app.my_progress';
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
        this.chartRef = useRef("Chart");
        onWillStart(async () => {
            await loadJS("/web/static/lib/Chart/Chart.js");
        });
        onWillUnmount(() => {
            if (this.chart) this.chart.destroy();
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
        this.state.catalog_list = exercise_catalog;
    }

    async loadChartData() {
        const records = await this.orm.searchRead(
            "fitness.set",
            [["exercise_id.catalog_id", "=", this.state.selectedExerciseId]],
            ["weight", "set_date"],
            {order: "set_date asc"}
        );
        this.state.chartData = records;
        this.renderChart();
    };
    async renderChart() {
        const canvas = this.chartRef.el;
        if (this.chart) {
            this.chart.destroy();
            this.chart = null;
        };
        if (canvas) {
            this.chart = new Chart(canvas.getContext("2d"), {
                type: "line",
                data: {
                    labels: this.state.chartData.map(r => r.set_date),
                    datasets: [{
                    data: this.state.chartData.map(r => r.weight)
                    }]
                },
                options: { responsive: true }
            });
        };
    };
}

registry.category("actions").add("display_progress", MyProgress);