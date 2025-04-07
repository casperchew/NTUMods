class ModsController < ApplicationController
  def index
    search = request.query_parameters[:search]
    @mods = Mod.where('course_code LIKE ? OR title LIKE ?', "%#{search}%", "%#{search}%").order(course_code: :asc)

    if request.query_parameters[:no_prerequisites]
      @mods = @mods.where(prerequisite: nil)
    end

    levels = [1000, 2000, 3000, 4000, 5000].select { |i| request.query_parameters[i.to_s] == 'true'}
    level_query = levels.map { |i| "course_code LIKE '__#{i.to_s[0]}%'" }.join(' OR ')
    @mods = @mods.where(level_query)

    if request.query_parameters[:DSAI]
      @mods = @mods.where("course_code in ('CC0001', 'CC0002', 'CC0003', 'CC0005', 'CC0006', 'CC0007', 'HW0218', 'MH1805', 'MH1812', 'MH2100', 'MH2500', 'MH2802', 'MH3500', 'MH3511', 'ML0004', 'SC1003', 'SC1007', 'SC2001', 'SC2002', 'SC2006', 'SC2207', 'SC3000', 'SC3021', 'SC4000', 'SC4020')")
    end
  end

  def show
    @mod = Mod.find(params[:id])
    @reviews = Review.where(course_code: params[:id]).order(created_at: :desc)
  end

  def search
    @mod = Mod.where(course_code: params[:search])[0]

    if @mod
      redirect_to mod_path(@mod)
    else
      if params[:search].blank?
        redirect_to mods_path(
          :no_prerequisites => params[:no_prerequisites],
          1000 => params['1000'],
          2000 => params['2000'],
          3000 => params['3000'],
          4000 => params['4000'],
          5000 => params['5000'],
          :DSAI => params[:DSAI]
        )
      else
        redirect_to mods_path(
          :search => params[:search],
          :no_prerequisites => params[:no_prerequisites],
          1000 => params['1000'],
          2000 => params['2000'],
          3000 => params['3000'],
          4000 => params['4000'],
          5000 => params['5000'],
          :DSAI => params[:DSAI]
        )
      end
    end
  end
end