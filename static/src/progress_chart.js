import { Component, xml, useState, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class MyProgress extends Component {
    static template = xml`
    `;
    setup() {
        this.state = useState({
            selectedExerciseId: null,
            chartData: [],
        });
        this.orm = useService("orm");
    }
    async fetchData() {
        const records = await this.orm.searchRead(
            "fitness.set",
            [["exercise_id", "=", this.state.selectedExerciseId]],
            ["weight", "workout_date"],
            {order: "workout_date asc"}
        );
        this.state.chartData = records;
    }
}

registry.category("actions").add("display_progress", MyProgress);