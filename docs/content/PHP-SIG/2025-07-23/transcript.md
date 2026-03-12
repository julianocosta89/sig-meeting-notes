SIG: PHP SIG
Date: 2025-07-23
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:12 Hmm.
**Nick Schuch** 00:16 Hey? How's it going.
**Chris Lightfoot-Wild** 00:19 Well, thanks. So you.
**Nick Schuch** 00:21 Yeah. Yeah. Not too bad. Not too bad.
**Chris Lightfoot-Wild** 00:24 Seen you in a little bit.
**Nick Schuch** 00:27 Yeah, yeah, I'm back into it. I went away for It was school holidays in Australia. So yeah, we we did a couple of weeks of caravan, so.
**Chris Lightfoot-Wild** 00:37 Nice.
**Nick Schuch** 00:39 Yeah, it was kind of our 1st big caravan trip. So we got, I've got me and my wife have 2 kids. So yeah, it was pretty fun stayed at a couple of places.
Yeah, it was like, 2,700 kilometers, 30 h of driving in total. Yeah, it's pretty cool.
So yeah, yeah.
**Chris Lightfoot-Wild** 01:02 What? A trip? Amazing.
Okay.
**Nick Schuch** 01:05 Yeah.
**Chris Lightfoot-Wild** 01:06 That seems like the safer option than camping, I guess. Really.
**Nick Schuch** 01:12 Oh, yeah, yeah, we yeah, we've done a little bit of camping. But yeah, it's so much, so much nicer. It was in the caravan.
yeah, it's because it was quite cold. So so luckily, all the places that we stayed were powered so you could run like a little heater. And then, yeah, vice versa, like we've done stuff in the summer, when it's hot and it's kind of nice, because you can just hop in and turn the icon on. So there's a little.
**Chris Lightfoot-Wild** 01:44 Yeah.
**Nick Schuch** 01:45 But yeah, so yeah, no.
Very much bought into caravan life. So.
**Chris Lightfoot-Wild** 01:56 Hey? How you doing, Bob?
**Ago Allikmaa** 01:58 Time.
**Bob Strecansky** 01:59 Php.
how's everyone doing there?
**Chris Lightfoot-Wild** 02:09 Yeah. Thanks.
**Ago Allikmaa** 02:11 Pretty good.
**Chris Lightfoot-Wild** 02:47 Guessing. We're waiting on a few more people. Because I think we said last week, we're gonna go through some kind of interactive, anything to the right.
**Bob Strecansky** 02:57 Yeah, we didn't talk about spi right? Or we're talking about something else.
**Chris Lightfoot-Wild** 03:00 Yeah, well, yeah, I think it was spi. So I'm guessing Sergey. And
**Bob Strecansky** 03:05 Yeah, we wanna wait.
**Chris Lightfoot-Wild** 03:06 For them. I'm gonna wait for them for that one for sure.
Okay.
**Bob Strecansky** 03:33 Brett said. He's sick and he's not gonna be here today.
**Chris Lightfoot-Wild** 04:08 I guess we could always start and just go through the regular issues. Prs, etcetera.
This is broken up yet.
**Bob Strecansky** 04:17 Sure works for me. I'll share my screen getting myself situated here. Sorry about that.
for all you, Mac people. I started using something called aerospace, and it's pretty awesome if you haven't checked it out yet.
**Chris Lightfoot-Wild** 04:46 Is the arrow or arrow. Sorry?
**Bob Strecansky** 04:49 a ERO. Space like the it's like it's a tiling window manager for Mac OS, that's pretty great.
Let's take a look here, open pull requests.
So there's a couple drafts put semantic conventions. Pr. I approve but myself. And oh, he added, some more stuff afterwards, let that be.
Let's see, let's see, here's bow.
**Pawel Filipczak** 05:40 Hey, guys.
**Bob Strecansky** 05:46 There's info factory. Someone had a lot of commentary.
Hold on, I guess.
**Chris Lightfoot-Wild** 05:55 Do you know if Sergey is joining today as well at all?
**Bob Strecansky** 06:09 So there's nothing here entered experimentation, coach, real action.
These are usually pretty easy to approve and manage.
So almost a 20 million nice work everyone good protest to kv, 2.
So a couple of things that are waiting progress.
Oh, I think that we can talk through some of these. Chris, you want to leave this? What's going on with 1436.
**Chris Lightfoot-Wild** 07:10 Well, that's the Sbi one
**Bob Strecansky** 07:12 Okay, well, that's what we're gonna talk about today. Look at that perfect timing.
**Chris Lightfoot-Wild** 07:16 Back to that one I share.
**Bob Strecansky** 07:19 And then let's see, what's this one working on span suppression looks like he's having conversations with about this. I'll leave that alone.
And then a couple left in to do.
Looks like things are chugging along this. So do you want to wait for Sergey to talk through the spi implementation or PAL you do you want? What do you think.
**Pawel Filipczak** 07:51 So you can reach him on the on the slack. I'm not. I'm not sure why he's he's not today on the meeting. Let I guess the reason is that we have some like free hands to this week in in our company. So.
We can do whatever we want. So maybe that's the reason. But anyway, you can reach out to him directly, and business in onslaught.
**Bob Strecansky** 08:15 Got it alright while we wait for him. Does anybody else have anything they'd like to discuss.
**Chris Lightfoot-Wild** 08:24 So should we message him once that sorry have you done that? Or.
**Pawel Filipczak** 08:28 Sorry I didn't understand you.
**Chris Lightfoot-Wild** 08:30 You say you want us to message him on psycho? Have you already.
**Pawel Filipczak** 08:33 Yes, just just reach out to him, or I will let him know that that you want to sync with him.
Yeah.
**Chris Lightfoot-Wild** 08:42 Just to see if we can still answer the call
**Pawel Filipczak** 08:46 Yeah.
**Chris Lightfoot-Wild** 08:47 I'll send him a quick message.
**Bob Strecansky** 08:49 If we have to punt that discussion to next week, too. That's totally fine.
**Chris Lightfoot-Wild** 08:54 Yeah.
**Bob Strecansky** 08:57 I know he was. He was very interested. So I want to make sure that he's around and available for that discussion.
**Pawel Filipczak** 09:03 Yeah, I was on vacation last week, so I'm out a bit a bit out of sync. So.
**Bob Strecansky** 09:08 That's okay. Hope your vacation won't work.
**Pawel Filipczak** 09:12 You know.
Thanks.
So maybe I'll share what I what I did.
**Bob Strecansky** 09:20 Oh, sure. Yeah, please.
**Pawel Filipczak** 09:21 Instrumentation. So I'm close to finish. Now, now, I'm working on instrumentation of the large objects.
so you can just put the files or whatever you want to the Postgresql, a database as a stream.
So maybe end of this week I will create that pull request for that.
And the second the second task is is the issue with the current instrumentation. So one of of the users found that the that the week reference to the to the current hand is is not existing prepared some work around. But I need to think a bit a bit more about that. How prevalent this kind of issues, and I don't understand why schedule had disappeared from them as as an object. So yeah.
I will spend a bit of time on that.
So that's all from.
**Bob Strecansky** 10:32 Cool.
That's it's not just, that's all. Those are great things. I'm excited for both of them.
**Pawel Filipczak** 10:41 Sorry I need to open the door. Let me back in the.
**Bob Strecansky** 10:51 Chris, you messed sugar.
**Chris Lightfoot-Wild** 10:53 I did do. Yeah, I've not had a response yet. I need.
It's shown as a sort of online status on slack, but might be head down, doing something else.
**Bob Strecansky** 11:04 We can do the classic American. Wait 15 min, and then you can leave. If your professor hasn't shown up yet.
**Ago Allikmaa** 11:11 I don't think that's just an American thing.
**Bob Strecansky** 11:16 Is that is that also everywhere else? I don't know. Maybe that was just me being a dumb American. But.
**Ago Allikmaa** 11:21 Yeah, we I was placed in Europe. In some places. We also have the same.
**Bob Strecansky** 11:27 I feel like they always put that in movies like the kids throw their pencils and their notebooks in the air and run out of the classroom at 15 past, or whatever.
**Chris Lightfoot-Wild** 11:36 Well, I did actually have something else to talk about. If no one else minded.
**Bob Strecansky** 11:41 Oh, Chris, the floor is yours, my man.
**Chris Lightfoot-Wild** 11:44 It was only in the slack channel this week someone had asked about instrumentation via hotel distributions.
Let's see me.
**Bob Strecansky** 11:54 Yeah.
**Chris Lightfoot-Wild** 11:55 See, there's a bit of a conversation on that and Maybe it was lacking on the documentation side that we have.
There's kind of some. I guess it's not like open telemetry. It's like vendor specific. But one of those obviously, is the elastic one.
So I was just having a look around at that, and I guess I had some questions.
maybe, about how some of it worked. And, Powell, I don't know if you mind it. If I just threw some kind of stuff out, or this wasn't the forum for it. But would you mind if I ask some questions about that as a sort of discussion point, just to try and better understand.
**Pawel Filipczak** 12:32 So sorry I didn't understood what was talking about. My Internet is sluggy. So.
**Chris Lightfoot-Wild** 12:39 Yeah, I was just saying, if I've got some questions about the elastic hotel, Php, Distro.
**Pawel Filipczak** 12:46 Yeah.
**Chris Lightfoot-Wild** 12:47 I just wondered if it was alright to ask them or not, you know. Kind of ad hoc.
**Pawel Filipczak** 12:53 And and the question is.
**Chris Lightfoot-Wild** 12:56 Cool. Alright. So I've seen it looks like there's obviously, you've got an extension like a C plus plus extension.
**Pawel Filipczak** 13:04 Yep.
**Chris Lightfoot-Wild** 13:05 And from what I could tell, that is what is then calling like pretty early on like a pre in it. Bootstrapping stage.
**Pawel Filipczak** 13:14 Yep.
**Chris Lightfoot-Wild** 13:15 And then you've registered your own autoloader to provide the elastic specific classes which are obviously some kind of route level vendor directory. I believe.
**Pawel Filipczak** 13:30 Yep.
**Chris Lightfoot-Wild** 13:30 So I think, as I understand it, you're gonna have this applications installed separately, and they've got their own vendor directories. And then it's a root level vendor, Directory.
**Pawel Filipczak** 13:40 Yes.
**Chris Lightfoot-Wild** 13:41 And then all of the instrumentation auto instrumentation that you've depended on at the root level is part of the the root level composer for that, but I didn't understand how you've got like Slim and maybe curl in there and etc. But the auto loader didn't seem to handle loading that it. It looks like it only handles for elastic namespace, and then everything else would fall through to the application specific one.
**Pawel Filipczak** 14:13 So the it's so. How it works the elastic distribution. Can you hear me? Okay, cause your your voice is not not clear for me. But yeah.
so the elastic is bootstrapping the code, and he's loading the classes from the vendor directory bring by the elastic distro.
And so each and every class which is which is loaded.
It's loaded first.st So the same classes bring by your own vendor Directory from your your application won't be loaded because it's already loaded. So the that's that's the 1st case here.
So let's say we are first.st So we are loading the our. Our versions of the classes so it may, so it may lead to some mismatch between the versions. If your staff is required, requiring some other versions which is not compatible, then it may lead to to some issues.
and if you are logged in the then if you are loading something from your application or via your application auto loader.
then it should load additional classes automatically.
So if you are loading something and loading some other dependencies or other instrumentations, they should be loaded.
but you know it may, it may produce some conflicts.
and especially between the versions, because, if you are, for example, semantic conversions we are loading, and we are delivering the 1 30, and you want to load the 1 40, then then we will load the 1 30, and we can't. You know, bypass that. So yeah, that's that's an issue. If you're delivering some set of packages, then they won't. They will be loaded first.st But we are not loading each and every classes right, so it it they are all that on on demand.
without all order.
So I introduced some some feature in in the native part which is blocking, loading of the of the classes which exist in both.
So the the priority is from the elastic distro. And if it's not a not existing in the elastic. Then it's loading from the other sources.
Yeah.
**Chris Lightfoot-Wild** 16:52 It was just that I couldn't see.
For example, like with the slim one.
there's a custom auto order for the elastic part of it, but presumably that is then deferred to the application composer instead.
But they're a separate vendor directory.
So how? How does that bit know to look in your root level vendor directory? It looked like you've got an auto loader. That's kind of only cares about the elastic ones, but might have just misinterpreted it.
I would read it.
**Pawel Filipczak** 17:27 So if if someone is loading the slim, then the slim from the vendor directory of application should be loaded.
If I understood your concerns correctly.
**Chris Lightfoot-Wild** 17:40 Yeah. Sorry it wasn't. Maybe I could share my screen a second. If that's okay,
**Pawel Filipczak** 17:45 Yeah. Philadelphia.
**Chris Lightfoot-Wild** 17:47 You can watch an idiots try to stumble his way around bear with me a second.
**Bob Strecansky** 17:54 Wait. I'm not sharing my screen.
**Chris Lightfoot-Wild** 17:59 I'm I'm the idiot here.
there we go. So let's talk.
Yeah. So the the this part of the auto order here It's auto load code for class. And then early on, it's checking whether or not it's an elastic class.
So if the prefix matches.
That's the hotel. You load it in from the sort of root level vendor directory.
**Pawel Filipczak** 18:31 Yes.
**Chris Lightfoot-Wild** 18:32 But then, in your composer.
I'm I'm sure this all works as well. So I was just looking at the code and couldn't make sense of what was happening. So you've got like, you know, auto slim, for example. There.
but if you've not got that as an application level dependency.
I'd expect you know these will all be populated in the Root Level Vendor Directory. So when you're auto loader in your application.
or or rather, when the autoload mechanism kicks in. It looks like this. One won't handle that case and serve it from the root level.
**Pawel Filipczak** 19:10 Yes, so it so. If if your application is loading also the slim, then the E dot slim auto instrumentation will be loaded, and if your application is using the slim, and you don't need to add anything to your auto loader in the application. You don't need to add the auto instrumentation.
**Chris Lightfoot-Wild** 19:32 Do.
**Pawel Filipczak** 19:33 Because it will automatically load the instrumentation from the edit.
So the the autoloader is is just that in that outdoor loader class it's loading everything which is in the path of the of the delivered Vendor Directory. So if you are, if you are installing the the path we are all during the build of the the system packages we are generating the we are running the composer install.
and you are packaging the result of of the I mean the the vendor folder into subdite, some directories into into the opt elastic, and so on. Folder.
**Chris Lightfoot-Wild** 20:17 Okay. Yeah.
**Pawel Filipczak** 20:19 Installation. Right?
So then, it's checking the path, and it's loading everything. What? What's inside the the our vendor folder.
**Chris Lightfoot-Wild** 20:32 Yeah, I I get that. But I guess it's just that.
Would you have to explicitly, then have those dependencies in your application as well.
**Pawel Filipczak** 20:41 No in your application now. So everything which is specified in in the elastic composer will be loaded, and if and that's it, so, no more instrumentations will be loaded.
**Chris Lightfoot-Wild** 20:57 I guess I guess I'd probably have to try it, because I feel like I'm laboring on on this a little bit sorry. So apologies to everyone else. If this is.
this is already clear.
**Pawel Filipczak** 21:06 So those those all of those packages here required here they are delivered by the package. So if you are using their Pm. Or Dep, or whatever else package or ipk.
then it will be extracted into the opt folder on your system.
**Chris Lightfoot-Wild** 21:23 Yep.
**Pawel Filipczak** 21:23 The elastic path, and we are delivering the vendor folders for each. P. Supported Php version. So inside the installation for that there is a vendor underscore 8, 0 8, 1, 8, 3, and 4, and so on. Right.
**Chris Lightfoot-Wild** 21:40 Okay.
**Pawel Filipczak** 21:41 And this Php. Code is during the Bootstrap is checking the version of the Php. Are using. And it's adding the path. This particular path of the of the vertical. For example, for the Php. 8 or 3, it's adding the vendor underscore 8 dot. 3, and it's loading the data from there. So it's it's it's triggering the the auto loader to to, and it's adding the auto loader hook to to load classes from there.
**Chris Lightfoot-Wild** 22:12 Oh, okay, so is that that's not necessarily here, but somewhere else. That's.
**Pawel Filipczak** 22:15 Yep, yep, yep, yep.
**Chris Lightfoot-Wild** 22:18 Okay, sorry. I just. I kind of, I guess phoned it on the file. And I was like, I'm not sure what's going on.
**Pawel Filipczak** 22:24 You show you the code because the the screen is a bit blurry, so I need to wait a bit.
**Chris Lightfoot-Wild** 22:34 Zoom in a little bit.
**Pawel Filipczak** 22:36 Yeah, let me let me check. I will, I will! I will! I will show you. But.
**Chris Lightfoot-Wild** 22:41 Your screen.
**Pawel Filipczak** 22:41 Okay, let just let me give me one second.
I will share my my screen. One sec.
**Chris Lightfoot-Wild** 22:57 So I was quite interested in seeing if could replace what we've already got with.
Yeah. So this.
**Pawel Filipczak** 23:20 Can you see the window.
**Chris Lightfoot-Wild** 23:22 Yeah, you can see that.
Well, a a stretch is quite small, but.
**Pawel Filipczak** 23:27 I will, I will make it bigger.
Is it good now.
**Chris Lightfoot-Wild** 23:35 Yeah, that's perfect. Thank you.
**Pawel Filipczak** 23:37 So probably, which quarter it was so here in the Php. Parked facade.
**Chris Lightfoot-Wild** 24:00 Okay.
**Pawel Filipczak** 24:00 Why, there is a register of order.
and the here we are generating the the pop to the, to the folder of the installation. So it's just checking where, from where the where the file sits.
and we are generating the path to the vendor folder. I I can also. I will stop sharing and share it again, and I will show you on the file system how it looks like, okay.
**Chris Lightfoot-Wild** 24:26 Yep.
**Pawel Filipczak** 24:28 Because I shared the window only. And now I share the desktop, the full screen. Okay, so so now it's generate is here. It's registering the the autoloader.
and how it looks like, so I don't have it. I don't have it installed, but I will show you in in the in the in my working Source Directory.
So you can see that the the we are generating, the those vendors folder and those folders.
those vendors. Folders are just in the same folder when the Bootstrap, the Php. File is.
and the and the the whole namespace. So there is a vendor folder for for the Php. 8 dot one. So let's go there, and you can see there is everything here and there. There is a autoload file, so we are just registering to load that files with this autoload.
and because we are registered as a first, st so our classes allowed so from our distribution allowed us are with the highest higher priority.
**Chris Lightfoot-Wild** 25:45 Okay.
**Pawel Filipczak** 25:48 And in the real world scenario during after installation of that folder. The this path will be in the opt elastic. Folder.
Okay. Elastic key. Dot. Php, something like that right?
**Chris Lightfoot-Wild** 26:02 Yep.
**Pawel Filipczak** 26:03 Yeah. And to do that, we have the we have the script which is generating the.
So you can also use it locally. So you can use your let's say, source code a copy.
And to do that, we are just generating that file, using that script which is generating the vendors folder using the docker containers.
And and this this is done during the build. But you can also do that locally to to generate those files, and it will, it will it will generate everything. And okay, then you will be able to to see it in the local folder.
And in the during my development, I'm setting up just the the in the I 9 file. I'm setting up the path to this Bootstrap file.
And after that it's loading everything automatically. So you just need to, you know, build it from sources. There is a development guide.
And here and you can just follow step by step, and you can, you know, build everything locally.
One of the steps is just to to add the dependencies here. So everything is described in the Development Guide.
Just, you know. Try the try to to play with it with it fully, locally. You can just install the package and it will work.
Yeah.
**Chris Lightfoot-Wild** 27:34 Oh, that's great. Yeah. Well, thanks for thanks for that.
**Pawel Filipczak** 27:39 Sorry could you say it again.
**Chris Lightfoot-Wild** 27:43 I? I said, Yeah, thank you for going through that. And apologies. I overlooked it.
**Pawel Filipczak** 27:48 Yeah, there's something with my Internet connection. It's it's stormy. And I'm using the 5G, and sometimes there are some issues with that when when it's raining. So yeah.
that's that's interesting that you can hear me going. Okay.
But anyway, if you have some questions and I didn't unanswer few questions. Please let me know on slack, and I will. We can just sync on zoom later, and I can show you.
step by step.
**Chris Lightfoot-Wild** 28:17 Yeah, sounds great. Thank you.
**Ago Allikmaa** 28:23 Did you do something there to like? Avoid issues with people trying to use same dependence with with different versions.
Like, let's say Castle, for example.
if it's the same namespace, and for some reason they need a different version that the one included in the vendor, once in the elastic agent and.
**Pawel Filipczak** 28:50 Yeah.
**Ago Allikmaa** 28:51 What could happen?
**Pawel Filipczak** 28:53 It may lead to to conflicts. Yes, that's true. If the Api is not correct, then it will. It may lead to to some issues. And we need to figure out how to solve that.
Yeah.
**Ago Allikmaa** 29:07 I guess, for, like open telemetry itself.
it would probably be fine that you cannot overwrite with different versions, but, like Castle, is generic enough that people might accidentally do it.
**Pawel Filipczak** 29:26 Miami.
So the-the- then the the reason for Gaza is sending the data right.
**Ago Allikmaa** 29:33 Yeah.
**Pawel Filipczak** 29:35 And we are so. The Gaza is not a good example, but it may. It may be something else. It doesn't matter. But with the Gaza.
We are not using that because we are delivering the background sending, which is fully native. So the classes which are using cases should not be loaded. They are still existing.
but it may, it might be with the other package, right? So.
**Ago Allikmaa** 29:57 But they are still like in priority for autoloading. So if they might get loaded, if the if people like use it in their own code, and expect their own version to be loaded when they use it from their own code.
**Pawel Filipczak** 30:15 So.
**Chris Lightfoot-Wild** 30:17 Does composer not already insert itself as the 1st auto loader. In like typical applications.
**Ago Allikmaa** 30:25 The whole point of this, that the agent is the 1st one.
**Pawel Filipczak** 30:33 Yes, he's registering the 1st out of order. Hook so, or or yeah, so the we can, of course, try to to solve that. But we are. We was discussing it with Sergey some time ago, and there is no good solution for that. So yeah.
**Ago Allikmaa** 30:53 Like one option would be that if the background sending is like the default option, then the autoloader pretends the guzzle doesn't even exist in the Vendor Directory, and you can like enable it, with some specific option.
**Pawel Filipczak** 31:13 Yeah.
But then we we would, we would need to, you know, provide some.
Let's say, list of the of the classes which are hard coded. So it's it. It cannot be generic enough, you know, to to implement that and make it, you know, easy. So of course, we can do that for this particular or other classes or libraries. But but yeah, at some point, we and have some issues. Yeah.
**Ago Allikmaa** 31:42 I think, like some at some point in the past, we discussed making a separate namespace, for, like the dependencies included in the agent.
**Pawel Filipczak** 31:55 No, that's 1 of the issue of the of the solutions. Yeah.
but it would require, you know, let's say, modify a lot of effort during the installation, the packages to change the namespaces and and generating the code and adding some, you know scripts which you know French is there understood the code and replace the namespaces. So if it's possible but I think it's the best solution, the the best solution, because it will solve all of the issues.
But still it. It's very complicated.
**Ago Allikmaa** 32:39 Especially testing that it works in a very.
**Pawel Filipczak** 32:44 Yeah, that's that's that's true.
So yeah.
**Chris Lightfoot-Wild** 32:53 Yeah. Well, I'll try. I'll try and give it a go at some point, because I'm I'm quite interested. So thank you for.
**Pawel Filipczak** 32:58 The point is that just ping me anytime on on slack and see if I be in front of of my computer, then I will. I will try to help.
**Chris Lightfoot-Wild** 33:10 So that's.
**Pawel Filipczak** 33:11 Sometimes I'm not responding, but I will. I will let you know.
**Chris Lightfoot-Wild** 33:15 That's right. So because this is part, this is the main bit. That's the proposal for donation, I think is is.
yeah. So that's why I was kind of thought.
Maybe that would answer the question in future. If that becomes the if we have an official Php Distro or something.
I guess that's the the goal. There.
**Pawel Filipczak** 33:34 M.
**Chris Lightfoot-Wild** 33:36 Nice.
**Pawel Filipczak** 33:37 Yeah.
**Chris Lightfoot-Wild** 33:38 I know there's an aws one as well, but I've not.
I mean that that must have been around for a long time, and it's had no sort of recent mentions or anything, so I don't know if it's maintained or not. But.
**Pawel Filipczak** 33:50 Yeah, it's weird. Maybe it's maybe it will be easier to, you know, handle some issues with the spl. And then.
yeah, I need to think about that, how to solve, how to solve that issues. Maybe Spiel can help that with the, you know, loading the classes. But.
**Chris Lightfoot-Wild** 34:09 For the most part you deferring to Php. Instead of doing it native extension for the for the auto loading right.
**Pawel Filipczak** 34:20 Yeah.
**Chris Lightfoot-Wild** 34:22 Okay.
**Pawel Filipczak** 34:26 Native part is just doing compilation of that Bootstrap, Php. File. And it's calling the static method from that from that class.
And so the native part.
It's not, you know, complicated in in case of bootstrapping. So everything is done in in the Php, yeah.
And and the the only one feature which is implemented in the in the native part is to block the conflicts on the functions, because if the function is implemented.
so you, if the class that is is loaded with the autoloader. Then autoloader is is detecting that the class is loaded, and it it it will not call the the. It will not load the the class file with the implementation of the class right? But with the functions it's not so easy. So you can have duplicates in the functions, and then you will get the the fatal error, because the function is already implemented.
and to prevent that, there are few few functions implemented in the in the P in in the hotel implementation.
and to avoid conflicts, I I implemented the the protection for that. So if the if we are delivering some something from the our source Code Directory.
Then it's it won't be loaded from the other source. So yeah, that's the only only protection we made in the native part, but everything else is.
It's pure Php.
**Chris Lightfoot-Wild** 36:10 And and sorry. I guess one final thought on that. If you just have an imaginary typical composer install and then your you've just got an index file in the 1st line require vendor, slash, autoload dot php, then obviously, that battery bootstraps composers, auto loader, which bumps itself to the front by the foot. But then, if you're using the elastic hotel extension.
Is that essentially room first, st before even composer kicks in, and the the very 1st part of the script is your initialization, and it bootstraps.
**Pawel Filipczak** 36:54 Yes.
**Chris Lightfoot-Wild** 36:55 Inserts itself as a 1st compose auto loader. Sorry, but then, after that it looks like composer boots you down to second.
**Pawel Filipczak** 37:05 Yes.
and it will do exactly how it works. So there is very secure. So 1st register this 1st code during the Delta order. Of course you can set the priority. There is an option to set the priority.
but by default the 1st register is is 1st called so. In that case the classes from the elastic distro will be called.
and then the the everything from the other of the older hooks will be just dropped. If the if the class is already loaded.
But for the functions, it's not working like that. So the the there is no files for the function. So if you have a class implemented in the file, and you have the free for free for function in that same file outside the outside the class. Then there will be a conflict.
If you have a class A and the function B outside of the class, then it will it will fail, so that there is a reason for the protection for that. So if you have the function, which is.
it's blocking the the loading of the functions. If if they already already delivered from the elastic source code.
So basically speaking, it's not loading the same files.
It's it's it's comparing the path, say, until the path part of the path.
It's the same.
It's just dropping the the vendor, the the files from the vendor for folder of the application.
**Chris Lightfoot-Wild** 38:39 So ideally, I mean is that are you happy, being second behind the composer auto? Or would you prefer to actually be first? st And I have final say over.
If you are wanting to load your Distro specific, it's interesting.
**Pawel Filipczak** 38:55 If we are first, st it's so, it's solving a lot of issues, because we can easily schedule the.
**Chris Lightfoot-Wild** 39:01 The open telemetry classes, which are.
**Pawel Filipczak** 39:06 Just delivered by the open telemetry, like, you know, senders, exporters, whatever. Right?
And if we'll be logged at first, st second, it it will make things more difficult. So of course it's possible. But then we'll need to allow changing of the or replacing the implementations via the via the SDK. So if you allow to change some implementations or just replace them on the flight, then there is no reason to, you know, to to be the 1st one. We will just, you know.
call some function which replace the the implementation. So on some interfaces. Right? And that's it. But now we are just trying to schedule.
Yeah.
**Chris Lightfoot-Wild** 39:58 Yeah, suppose probably, either way, you're gonna get the same problem with maybe incompatible one way or the other, depending on application or like site wide version in.
**Pawel Filipczak** 40:09 Yeah, it. It may solve some issues. If you will be the last one.
then we can, of course, solve a lot of issues with the with the race right on on the loading of the of the classes.
Yeah.
but still still there, at some point with the current implementation, will will lead into some conflicts with the version, because now the the company, if you are deploying the application you're calling composer in install.
and you you have the the all of the dependencies and versions you know.
compared together, and they are in the in the latest versions, and we should work together. If not, you will get the notification that you will break right the installation with this solution. It's not so easy to to solve that. So one of the issue, or 1, 1 of the best solutions is just to bring deliver the additional namespace.
And yeah, so we can, of course, do that somehow. Yeah.
or either by modification, the code, or during the compilation of the code. For example, if you will deliver something with the E dot, we cannot check, modify everything on the ist level. Right? So during the compilation, we can inject the the namespace into the into the compiled classes.
So that's 1 of the easiest solution. I think it's it's it should be easier than you know.
**Chris Lightfoot-Wild** 41:44 Modifying the.
**Pawel Filipczak** 41:46 The the files on the installation. Because, yeah.
In the Php. We have everything the lexical parsing, and then we are, we are, we are.
**Chris Lightfoot-Wild** 41:59 Bye.
**Pawel Filipczak** 41:59 We have the Ast tree, which is quite simple.
So maybe that's as one of the solutions to prevent the the issues.
**Chris Lightfoot-Wild** 42:13 Cool. Alright. Well, thanks very much for that. And it was very interesting for me, at least hopefully it will benefit too.
**Pawel Filipczak** 42:23 Yeah, if you have any questions, just let me know.
**Chris Lightfoot-Wild** 42:28 I guess. Is there any movement on that issue at all? Or is it still waiting for the technical committee?
Yeah.
**Pawel Filipczak** 42:35 So we passed 1st step. So, yeah, I hope it will. It will move forward.
**Chris Lightfoot-Wild** 42:42 Go ahead.
Thank you.
I'll stop asking questions. Now then, Bob.
**Bob Strecansky** 42:54 Like your questions alright. Anybody else have anything before we adjourn.
**Chris Lightfoot-Wild** 43:03 Do, I guess? Do we want to stick the desperate, I think, on next week's agenda, so we can see. Cause I think.
**Bob Strecansky** 43:08 Yeah, well.
**Chris Lightfoot-Wild** 43:08 I felt like Sean was perhaps interested as well, but to real life getting away.
**Bob Strecansky** 43:14 I'll make a proactive agenda for next week and put that on.
**Chris Lightfoot-Wild** 43:18 Cool.
Thank you very much.
**Bob Strecansky** 43:22 Alright. We'll see you on the Internet.
**Ago Allikmaa** 43:25 Go ahead!
**Pawel Filipczak** 43:26 Explain.
