import { Injectable } from '@nestjs/common';
import { Whisky } from './interfaces/whisky.interface';

@Injectable()
export class WhiskysService {
    private readonly whiskys: Whisky[] = [
        {
            name : "The Glenlivet Captain's Reserve",
            type : "Single Malt Whisky",
            brand : "Glenlivet",
            country: "Ecosse",
            region: "Speyside",
            degree: 40,
            dateIn: new Date(2020,12),
            dateOut: new Date(0)
        },
        {
            name : "Togouchi Kiwami",
            type : "Blended Whisky",
            brand : "Togouchi",
            country: "Japon",
            region: "",
            degree: 40,
            dateIn: new Date(2020,10),
            dateOut: new Date(0)
        },
        {
            name : "Finloch Easy Dram",
            type : "Blended Malt Whisky",
            brand : "",
            country: "Ecosse",
            region: "Highlands",
            degree: 40,
            dateIn: new Date(2019,10),
            dateOut: new Date(0)
        }
    ];

    findAll(): Whisky[] {
        return this.whiskys;
    }
}
