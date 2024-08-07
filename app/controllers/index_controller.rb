class IndexController < ApplicationController
  def post
    course_code = request.request_parameters[:course_code]
    @mod = Mod.where(course_code: course_code)[0]
    if @mod
      redirect_to mod_path(@mod)
    else
      redirect_to mods_path(:search => course_code)
    end
  end
end
