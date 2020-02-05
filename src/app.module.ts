import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { WhiskysController } from './whiskys/whiskys.controller';
import { WhiskysService } from './whiskys/whiskys.service';

@Module({
  imports: [],
  controllers: [AppController, WhiskysController],
  providers: [AppService, WhiskysService],
})
export class AppModule {}
