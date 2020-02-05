import { Controller, Get } from '@nestjs/common';
import { WhiskysService } from './whiskys.service';
import { Whisky } from './interfaces/whisky.interface';

@Controller('whiskys')
export class WhiskysController {
    constructor(private readonly whiskysService: WhiskysService) {}
    @Get()
    async findAll(): Promise<Whisky[]> {
      return this.whiskysService.findAll();
    }
}
