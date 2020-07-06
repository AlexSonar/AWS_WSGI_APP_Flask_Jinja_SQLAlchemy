var gulp = require('gulp'), 
		sass = require('gulp-sass'); 

gulp.task('sass', function() { 
	return gulp.src(['venv/src/templates/static/sass/**/*.sass', 'venv/src/templates/static/sass/**/*.scss']) 
		.pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError)) 
		.pipe(gulp.dest('venv/src/templates/static/css')) 
	});

gulp.task('watch', function() {
	gulp.watch(['venv/src/templates/static/sass**/*.sass', 'venv/src/templates/static/sass/**/*.scss'], gulp.parallel('sass')); 
});

gulp.task('default', gulp.parallel('watch'));
