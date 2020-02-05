import { Test, TestingModule } from '@nestjs/testing';
import { WhiskysController } from './whiskys.controller';

describe('Whiskys Controller', () => {
  let controller: WhiskysController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [WhiskysController],
    }).compile();

    controller = module.get<WhiskysController>(WhiskysController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
