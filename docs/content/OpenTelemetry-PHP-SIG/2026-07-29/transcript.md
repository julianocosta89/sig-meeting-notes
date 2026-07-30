SIG: OpenTelemetry PHP SIG
Date: 2026-07-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Bob Strecansky** 01:52 Hey, Jerry.
**Jerry Ting Fung Leung** 01:54 Hello, Paul.
**Bob Strecansky** 01:56 I feel like I'm meeting a celebrity. I've talked to you online so many times, I've never seen you in person.
**Jerry Ting Fung Leung** 02:01 Yeah, yeah.
**Bob Strecansky** 02:04 Where are you… where are you located in the world?
**Jerry Ting Fung Leung** 02:07 I'm located, on… at the… at the western side, so right now it's 5 AM, in the morning.
**Bob Strecansky** 02:14 Oh, jeez.
Oh, thank you for joining.
**Jerry Ting Fung Leung** 02:21 And so that's why I most, mostly don't join this SIG meeting, because it's too early, but… It is.
when we have some important things to discuss, yeah, I can still, make the time.
**Bob Strecansky** 02:36 Yeah, we might need to revisit the timing, because we have… one of the other maintainers, Brett, lives in Australia, and I live on the East Coast, and other people live in Europe. It's like, there's no good time for everyone, and we don't want to have two SIG meetings, because that's much of a pain in the neck, so…
**Jerry Ting Fung Leung** 02:53 Yeah, I know that.
**Bob Strecansky** 02:55 Indeed.
I'm gonna also draw… I'm gonna also join the other Zoom, just on my phone, just to see… make sure that nobody's going to the old one.
Where on the West Coast do you live?
**Jerry Ting Fung Leung** 03:18 Excuse me.
**Bob Strecansky** 03:20 I said, where on the West Coast do you live?
**Jerry Ting Fung Leung** 03:22 Oh, Vancouver.
**Bob Strecansky** 03:24 Oh, very cool.
Yeah, we're on… we're on the… we're in the… Jerry and I are in the new, like… Sounds good. See you there.
So, yeah.
They're coming.
**Jerry Ting Fung Leung** 04:18 Sure.
**Bob Strecansky** 05:07 Oh, so, Jerry, the way we normally run this meeting, just so you… to catch you up to speed, we normally go through the agenda topics that we have listed here. You can feel free… looks like you've added stuff here already, but you can feel free to add stuff as we talk through it, and then we'll go through all the open, PRs and issues in the repos, and then we sort of take it from there.
Good day, Chris, how are you?
**Chris Lightfoot-Wild** 05:29 Yeah, good, thanks, how are you?
**Bob Strecansky** 05:32 I, you know, living the dream.
**Chris Lightfoot-Wild** 05:33 Yeah. Hey Joey, nice to meet you.
**Jerry Ting Fung Leung** 05:36 Yeah, nice to meet you too. Yeah.
**Chris Lightfoot-Wild** 05:39 Yeah, did you have a good vacation, Bob?
**Bob Strecansky** 05:42 I did. I had a… we had a really nice time, except for our flights were… I've lived in Atlanta for 15 years, I've never had a flight canceled. We had two canceled in a row. Wow. Yeah. Inclement weather.
No, seriously. Inclement weather.
**Chris Lightfoot-Wild** 05:59 Wow.
**Bob Strecansky** 05:59 But we made it, and… The weather was beautiful. It was, like, between 15 and 20 the whole time, more or less.
**Chris Lightfoot-Wild** 06:10 Nice.
**Bob Strecansky** 06:11 Yeah. It's Sergey.
Alright, I think… is this everybody? Is, Pawel gonna come join us today? Is there a good idea?
**Sergey Kleyman** 06:23 I can ask him,
**Bob Strecansky** 06:27 We can get going, and he can join us for once.
Alright, from Severin, Zoom meeting link changes. Check, we did that already. I updated that workflow, Chris, that you had mentioned in the Slack channel, so…
**Chris Lightfoot-Wild** 06:45 Next.
**Bob Strecansky** 06:45 every week we should get that, because that's the only way that I, like, I've tried to use the calendar invite a bunch of times, and I just end up losing it, or, like, removing that Google Calendar for the rest of my calendar. I found out that Slack link's the only thing that's consistent for me.
**Chris Lightfoot-Wild** 06:58 I now have two calendar invites, so I have to remember to delete But, yeah, sometimes.
**Bob Strecansky** 07:05 We'll get there.
Alright, get split workflow changes. Chris, you have this on the agenda.
**Chris Lightfoot-Wild** 07:13 Yeah, so, last week, Pawel and I were just talking a bit more about the contrib, split, to try and get the pipeline toward green, and this is one of the… one of the bits that kept falling over when… When you do a new, workflow, and put it in that other repository. It would just sort of complain at you that it couldn't automatically add that itself under the previous token that was in use on the OpenTelemetry repo?
But I don't know who set that up, it was, you know, possibly, previous, maintainer or something.
So yeah, this one has moved to, using the OpenTelemetry bot. I tried the… the proper OTEL bot that lives under the OpenTelemetry organization.
But that isn't scoped correctly. But I've made one under the OpenTelemetry PHP organization.
That is for our own usage.
So, the credentials for that are added to this repo, And then this allows that workflow to, assume that role, I suppose, and then… It's got the permissions, then, to create new repositories and serve the workflows.
**Bob Strecansky** 08:31 Wonderful, thank you. I can review… I can review this later, and we can… Cool.
**Chris Lightfoot-Wild** 08:36 And then there was a few more, I just did two of the instrumentations to move across, and if that fixes some of the issues that we've seen with that.
We'll just rattle through a few more.
**Bob Strecansky** 08:47 Sounds good.
I'm… I will put this… I'll put this at the top of my queue for today.
**Chris Lightfoot-Wild** 08:54 There was also… I left a note on there with a link to the communities thing, that you can create, like.
org, sorry, SIG-specific… Hotel Balls.
But I'm not sure that… I wasn't sure that would work for us, because it's in a separate org that we're targeting, but I'm not entirely certain. But I thought, well, this works, and it gets us, like, a bit further, and then we can always check that later if we need to poke it around a bit.
**Bob Strecansky** 09:22 I am, man, it'll get you every single time.
Cool. Cool. Well, thank you for… thank you for that.
**Chris Lightfoot-Wild** 09:31 No worries.
**Bob Strecansky** 09:32 Alright, Jerry, do you want to talk through the Kubernetes OTel operator?
**Jerry Ting Fung Leung** 09:38 Sure. So… so, so, how can you open that up?
**Bob Strecansky** 09:43 Oh yeah, sure.
**Jerry Ting Fung Leung** 09:44 Yeah.
Oh, okay. I can share my screen, yeah.
And this one.
Yeah, do you see my screen?
**Bob Strecansky** 10:06 Not yet.
**Jerry Ting Fung Leung** 10:07 Yeah, okay.
**Chris Lightfoot-Wild** 10:08 Hey, Paul.
**Bob Strecansky** 10:09 Okay.
**Jerry Ting Fung Leung** 10:10 Okay, good.
**Bob Strecansky** 10:10 Oh, it's it.
**Jerry Ting Fung Leung** 10:11 Yeah.
So… so, I think… I think last month, I, tried to propose a change to… to the operator code, so we can… we can try to inject the auto-instrumentation PHP to… to… to Kubernetes operator, so… but… But there's a question… actually, a pushback from the operator SIG that.
they cannot accept, the auto-instrumentation PHP, Docker image anymore, just like other, other languages they did in the past. So, Because the reason is, they think we are building… building the… the library, and building the library there, so… so, it's just some few lines, compose installing some package, and also to try to install… try to set up the OpenTelemetry, C extension there. And, that's why… that's why I approached to you guys that, hopefully can find some place to… to host this… this image, so they… so the operator code can, can do a Docker pull from… from… from the GitHub, container registry, or… or the Docker… docker… Docker Hub, so… so they can… so I can move forward to this PR. And, the… the Docker image itself is not… that hard to understand is just try to, set up the OpenTelemetry C extension per each, version, of PHP.
And, just set up the extension nicely, and make sure, the… the OpenTelementary INI file is in place.
And… So that it can work with the operator code.
So, so the inject… so I can talk a little bit more about the injection code.
And… Actually, the injection code, the key is to use the PHP INI doc scan directory to… to include the C extension.
The extension and also the packages.
And, and also, the other key is to use the auto-prepen file to… to include the autoload.
the… the packages, the autolo, so that we… we don't even need to touch the user application composer of JSON in order to, set up the instrumentation.
And, and here, the challenge is to, try to figure out, the… the correct… the correct OpenTelemetry C extension, because it is built in C, and there's different… different build options for that, such as the PHP version, the threat safety, and also the Linux or Alpine, variation. So, I… I use that.
I, basically, will run… We run a, A script for… for the user application, so that, we can So this is the script to try the best effort to… to detect, the fresh safety, the… the API version, and… and the standard C or muscle C for… for the… for the UPSA application, and then use another other, shell script to copy, those things, correctly to, to the, to the place, and then set up the… the INI to… to make sure everything is load, and… so they try to inject the code. So this… so this is the logic behind, and right now, just… I think the… the question is, I think there are two questions, so… so it's… I think the first question is, should… should OpenTelemetry PHP, community, should host… host this image. This is the first one, and the second question is, where should this Docker image, place in… in the OpenTen… under the OpenTelemetry PHP repository? So… so these are two questions.
**Bob Strecansky** 15:15 Thanks for the explanation there, Jerry. That clears up a lot of things.
So, my first question back to you is, have you looked to see what other SIGs do for this? I would assume that they host them all in GHCR somewhere.
Because I don't think… I don't know that we have a Docker Hub, corporate… license thing or whatever, I'm not sure, but I'm going to look, too, to see where other SIGs do this. I would assume that they have, like, a separate repo in their, in their respective SIG. If that's what we need… if that's what we need to start this, you could… we can open a… an OpenTelemetry community issue that, If… I'll share my screen again, if you don't mind.
**Jerry Ting Fung Leung** 16:01 Sure.
**Pawel Filipczak** 16:02 Surely we have the Docker account, and you can request in the community repository to create a space for that.
But, I, I guess Trask is, is handling that?
And for the distro he created, for the OpenTelemetry PHP distro, he created a Docker Hub account, and.
**Bob Strecansky** 16:23 Oh, did he?
**Pawel Filipczak** 16:24 Yep, yep, and so we have a space there, and we can publish the Docker images there. So we are using that to publish the Docker images for the built environment, to store the compiler and so on, to build the distro.
So, I guess you can reach out to him directly and get some, you know, clues, how to… about the naming convention, or just create issue in the community repository.
**Chris Lightfoot-Wild** 16:50 Is there a reason, then, we didn't just use the GitHub content registry? Because we do that already in our other stuff, don't we? Or is it just so we could do both? Are we pushing it to both?
**Jerry Ting Fung Leung** 17:01 I see other languages do both, the GitHub Container Registry and also the Docker Hub, so they provide, two… two-way to… to pull that, auto-instrumentation image. And actually, we can, use maybe some popular language auto-mentumentation, Java, as a… as an example. So, they did, yeah.
**Chris Lightfoot-Wild** 17:27 I have a layman's question, if that's alright. How does this differ, then, to the distro? Because I guess I don't really understand how the operator works, as a first, sort of, point.
But if it's using the entry point to load its own autoloader.
When the user application runs, does it not also load its autoloader, and then there's two competing autoloaders?
Does that not have the same problem as what you had in the distro with… Not doing the shadowing, so you've got potential duplicates, or… so I could be way off here.
**Jerry Ting Fung Leung** 18:06 I haven't took a very deep look to the distro, but here is just So, so just try to add the PHP support, by using a very basic, OpenTelemetry approach. So, just use the C… try to use the current, OpenTelemetry C extension, and also the current package to… to… to do that. So, for… I think for… for vendor, so for vendors like… like, like us, and, actually, we… we will try to create our own auto, auto-instrumentation PHP image by putting in the company-specific logic, the package, and also the company-specific CS tension as well, to… together with the… OpenTelemetry C extension in order to work out everything. So, I didn't… didn't… didn't, took, the… the distro at the first place to… to set up an example. Just like other, they are just using the… for example, the Java agent, or the… the Python, the… the Python is true to… to… to where, so that… But I think the distro one should also work, because you see the loading point is just the AutoPen file, and also the PHP INI scan directory, so they are so… they are a very generic setting, and it should apply to other… other distro as well.
**Sergey Kleyman** 19:48 Maybe there's a confusion regarding what distro, maybe, Jerry, you're not aware. We have a… maybe you saw the repo that's called Distro.
So it's not like distro by other companies, we have a distro that's part of the OpenTelemetry. But just to clarify the Chris's question, since I started to work on the operator, which Jerry's continued, and I'm more or less aware of both. So they have… they answer a little bit different use cases. So, distro… you still need to install it on the host where you want to monitor your PHQ applications.
versus operator, you don't need to do any changes to your container image where your PHP application is defined.
You just take your image as it is, it doesn't need to be aware of OpenTelemetry at all, and the purpose of operator is completely… inject everything from outside without touching the image itself. So it's a little bit, kind of like, you can say, a next step above, even. So, basic SDK requires you to make changes to the application code, right? So it's the most invasive.
The second stage is Distro. It takes it to the next level, saying, okay, you don't need to change your application. You can install application on the host as it is, but Distro will automatically find it and automatically instrument it, just because you installed distro on the same host.
Operator, you can say that it's even third level. It says, okay, you don't even need to change your host, which in this case is a container. Everything will be injected from outside.
Right, so technically, if you didn't have the work that Jerry is working on, you would still need to install distro inside your container if you wanted to. It's true, you wouldn't need to touch your application, PHP application, but as part of your container instructions in Dockerfile, you would need to put a line that installs the distro.
Without it, it would not be able to monitor.
**Pawel Filipczak** 21:30 About 2…
**Sergey Kleyman** 21:30 So, this piece is… okay, please go ahead.
**Pawel Filipczak** 21:33 You can also, sorry for interrupting, but you can also create an operator image, which will install the distro in the…
**Sergey Kleyman** 21:40 Exactly. Now we're talking about, can we combine these two things, because some of the parts that GRE tries to solve, and it also touches what, Chris, you touched, what happens if we take Jerry's solution and try to apply it to maybe an application that already has its own OpenTelemetry bundled with it?
then there will obviously be a conflict between those two, right? Some OpenTelemetry SDK instrumentations, they will come from outside, from operator, or from that image that Jerry showed us, and obviously then there will be also a part that comes with the application itself. So, potentially, they can clash.
So the way Distro solved it is by shade doing the dimension.
So, yes, Distro can be combined with… combined with the work that ZR is doing, and then you can get all the solutions that we already implemented in Distro.
So they don't… you won't need to reimplement them again for the operator, but we can see it as a next step, right? So whatever work Jerry is doing, it needs to be done, let's say, maybe not the work on the… on the extension, but most of it still will need to be done. And distro, as it is, cannot be used, right? Pawel, you probably will agree with me. Distro still the way it… it needs to be installed.
So if we want to use it as part of the operator, we will need to adapt it a little bit. Not something serious, but… because there is no installation here, we just need to bring it as the files.
With the sidecar image, kind of, that is being shared with the main container.
kind of like as files. So we will just need to adapt it, but I agree that whatever questions you ask about, potential clashes and the shader that is implemented in distro, to solve that problem of the clashes.
Yes, that solution can be taken, and either the whole distro can be used for the operator, or some pieces of the distro can be used just to solve this problem.
I hope I answered your questions.
**Chris Lightfoot-Wild** 23:40 Yeah, so does that mean that there's potential that things can get double instrumented, then? If, like, the way you use the… obviously, they've got, like, the vendored, composer, directory, but then the application one as well, they both auto-register themselves.
Presumably, the operator one goes in first.
Registers some stuff, then the application one jumps ahead of it, because it prepends.
And then you've got an unusual combination of both of them of in some of the instrumentation, they just use the autoload files, don't they? So they inherently run, like, very early on.
And some of them call, like, register on instrumentation in a static way.
And do they then double instrument, like, functions?
**Sergey Kleyman** 24:25 Right, so the question is how you see it, like, what would you want the result, the expected behavior to be in this case?
Because in some cases, you do want this double instrumentation, what do you call it? Because if, let's say, application brings some unique instrumentation with it, you do want that instrumentation to be combined with the spans that are being produced by operator, right? So it all depends, I guess, yeah, so Pawel might, give more background.
But I think recently we added, after shadowing, because after shadowing, you essentially broke those two worlds apart completely, right? So whatever application did was completely separate from whatever was done by Distro.
But recently, we bridged that. So whatever application is doing is now connected, so you get the correct relationship between spans, like parent to child-wise.
Yeah, so it's all about… but obviously, you will get double, yes. If you package in both cases, you will get PDO instrumentation, you will get double PDO… am I correct, Pawel?
You're used to mute.
**Pawel Filipczak** 25:27 Yes, yes,
**Sergey Kleyman** 25:28 Yeah, so… so if you really want to be completely, like, get the perfect picture in this case, yes, you will need to remove the… whatever instrumentations you know that come from outside, like PDO. You will need to remove it from your composer JSON for the application.
But if you have some unique packages that you know that are not coming, you can still keep them, or maybe you even have maybe manual instrumentation inside your application by calling API directly, right? You might still keep it, and then it will integrate seamlessly with whatever is done by outside.
So again, this is what I said. If you want it for this operator as well, all this can be taken, because it's already implemented for the distro, all this already implementation can be taken from the distro and incorporated with the operator.
We just need to do that work to combine it all. But I think it can be done on top what Jerry is doing. So I think what Jerry's doing is a basis, it needs to be done, and then whatever these additional use cases that you mentioned, then can be… they can be added on top of that.
**Chris Lightfoot-Wild** 26:24 It's just, if it ultimately was going to go down the route of the distro form's a big part of it, and then the Docker image is just… basically the distro, copying some files into places. Do we need the separate It's a PHP.
**Sergey Kleyman** 26:38 It can be debatable, because the standard extension has wider applicability, it can support platforms that, distro… we didn't write power, like, for example, all kinds of exotic, like, IXs and all kinds of things that can build C, but maybe cannot build C++, or maybe if there's some limitations. So, we can talk about it, like, how we want to combine… I wouldn't say it's not, like, straightforward.
decision to make, just say, okay, let's use distro and not use standard extension, because if it was that before, we would advocate for that the moment we contributed distro upstream. We would have said, okay, let's absolute the existing extension, but it still has its use cases. So… I think it's worth discussing, you are definitely raising a valid point, how we want to… but yes, I agree, like, whatever work is done on distro, not use it for this case, because it's so similar, would be a miss. It's definitely worth using. Whatever is already done on distro, you use it for this operator as well.
We just need to find the right way to combine these things.
So maybe there will be two images, right? You can say, okay, if you really want to use some exotic thing, then we will… it will be built using standard extension, and then if you have standard things, like Linux, then it might use distro. So, we just need to find the right way to… to kind of…
**Chris Lightfoot-Wild** 27:58 If that's the case, then it does make sense, I guess, to have a separate operator repo that we can have different variants in, pointing to, you know, whatever dependencies you need to pull through.
**Sergey Kleyman** 28:09 I'm in…
**Chris Lightfoot-Wild** 28:09 Maybe that answers the question.
**Sergey Kleyman** 28:10 You can see it that way, but like I said, because operator by itself is not reasonably linked to distro, like I said, it can be built out of extension, like Jerry showed us, and the instrumentation is from Contrib.
So… I mean, depends, I guess, I mean,
**Pawel Filipczak** 28:30 I'm excited.
**Sergey Kleyman** 28:31 Go ahead, Dean.
**Pawel Filipczak** 28:32 how the instrumentation is not being picked, but now by the… by the JERIS solution. So, how you can choose which packages will be included, and will… how… how they will be… how to instrument it?
for example, PDO, or Carol, or… I don't… I don't know any other.
solution. So, how to choose which package will be included into the operator?
**Jerry Ting Fung Leung** 28:58 let me share again.
Cheap.
Only the code… oh, easy.
So right now, just… I just, proposed some very basic, basic packages, so this kind of…
**Pawel Filipczak** 29:22 vacation.
**Jerry Ting Fung Leung** 29:23 just, just bundle it into the Docker image, and when the injection, ingestion logic, triggers, so you just, try to mark the directory so that, the user application can, can see the There's, packages inside their things.
**Pawel Filipczak** 29:44 Okay.
**Jerry Ting Fung Leung** 29:44 it just provides a very basic idea, so… so I think most of the company use case is that they will just create their own, composer package, and also, set up their own… their own, C extension, no matter OpenTelemetry C extension and other extensions in this… in this directory.
And then, it will work, with the operator code to inject the instrumentation to use that app.
**Pawel Filipczak** 30:17 Okay.
**Jerry Ting Fung Leung** 30:18 Yeah, so here just shows very basic, basic, basic packages. But if you have other specific, or some special, special thing, you, you can always create your own auto-instrumentation PHP Images, but it just shows the fundamental usage.
**Pawel Filipczak** 30:40 Okay, thank you, thank you, got it.
**Sergey Kleyman** 30:45 Yes, it's similar to what we did in Elastic, right? So, we build on top of the existing, and we just adopted them. So, yeah.
Although I probably… it probably will involve a little bit more advanced user to do that, right? So… Obviously, the basic users would want just to, tell operator, like, tag the container so operator can kind of, like, be applied to them, and then they would expect the basic stuff to be working out of the box without them required building their own Docker images.
For the operator. But… this is more or less what we do in this store, right? We also have some predefined set of instrumentations. Yeah, it would make sense for them to be aligned as well.
like Chris said, the use cases are very similar.
So,
**Pawel Filipczak** 31:32 What they say?
**Sergey Kleyman** 31:32 ask, like, my, again, regarding which repo hosted, like, I agree with you, Chris, like, it sounds from outside that use cases are similar, but like I said, there is some subset that is not 100% the same, because if you would want to use it for curating systems not supported by distro, then you will have to go and build a standard extension and use that, and not the.
**Pawel Filipczak** 31:58 Thanks.
Exactly, so that's the main difference and advantage.
**Sergey Kleyman** 32:03 I think you're keeping it a separate repo, or separately, probably… and then, I think it's better to just let it start, you know, get it working, see how people use it, and then build better integration between Distro and Operator.
I think it will probably will be best then try to, you know, from the get-go, try to combine them already at this stage.
This is my point of view. You guys, please chime in if I'm maybe missing some.
**Chris Lightfoot-Wild** 32:39 Were you gonna say something, Pawel there, or… zip code.
**Pawel Filipczak** 32:43 But how to then make selection?
between two solutions. So, if you introduce two solutions, I mean that one and the distro one.
So, how to choose… Loosen later.
**Sergey Kleyman** 32:55 I mean, ZRA implemented a very interesting mechanism that can automatically detect your operating system, almost everything about it, right? So maybe we can, even at that stage, we can already know which components to use Now, obviously, effect, like, obviously then the question, okay, then why are we even using, like, if we can always use distro, why are we even using the standard extension, right? So we know why, right? Because we want to support more exotic platforms, but the price of it will be less features.
Stunt Extension doesn't implement some of the features, so how we documented that might be… so we will need to document to say, okay, if you're using Stanton platform, like Linux.
We will automatically detect it, and you will get all the features, right? Via this operator, if… when the distro is integrated.
If we detect that it's not supported by distro platform, then we will fall back to using standard extension, and then there will be less features.
But users don't need to be aware of it. It can be completely automated behind the scenes. So that's… that's… in that sense, Jerry's solution is really good for that.
I don't think we need to make this decision now, and it should not be visible in the future if we decide to integrate Distro into this.
**Chris Lightfoot-Wild** 34:15 That's all the.
**Sergey Kleyman** 34:16 But having the hosting, like, that's why I think keeping it flexible and hosting it separately from distro just allows more flexibility in this, when we… and when.
And if we do that, so, the only… like I mentioned in… on Slack is that additional effort to setting up the repo and all that, but I don't know how much effort it is.
**Bob Strecansky** 34:43 Shouldn't be too bad.
**Sergey Kleyman** 34:48 Also, just to clarify for me to understand, so if we decide not to even host the image on the GitHub, but only Docker Hub.
then the whole point of distro then goes away, or do we still want to use… to host the code that PHP specific, remove it from operator and host it in that repo?
So that new repo that you're looking for, Jerry, is it for dual purpose, both to maybe host the image, and also to host the code that builds that image?
**Jerry Ting Fung Leung** 35:17 I… actually, I'm looking for, just like other language did right now, so, So they… they have the packages, the operator, like the auto-injugmentation Java, so this is the docker image.
**Bob Strecansky** 35:37 That was published… that was published 5 years ago, though. I wonder if that's changed since then.
**Jerry Ting Fung Leung** 35:42 Yeah, sold.
**Bob Strecansky** 35:43 Oh, sorry, that one, that one.
**Jerry Ting Fung Leung** 35:45 That was… And also the… the Docker Hub… Docker Hub one, so let me… let me find that one for you.
**Chris Lightfoot-Wild** 35:55 But it was the…
**Jerry Ting Fung Leung** 35:56 Especially the same.
**Chris Lightfoot-Wild** 35:57 The maintainer said, we don't want to do this anymore.
**Jerry Ting Fung Leung** 36:01 Yeah, they…
**Chris Lightfoot-Wild** 36:01 other languages away.
**Sergey Kleyman** 36:03 But this is what I'm trying to understand. So, let's say if this is not even the issue, like, let's say just using Docker Hub, like, I don't know why Docker Hub is not good enough, like, why people want also GitHub, what does it… What does it do in addition to Docker Hub?
**Jerry Ting Fung Leung** 36:19 I think for… for basic usage Docker, the GitHub is good enough, but I see they… they publish in two places, so that's why I… I try to, see if PHP can do the same.
**Sergey Kleyman** 36:33 No, I'm trying to say, like, if you decide to only publish on Docker Hub, will it save you the effort to create a separate repo? Can you still host all the code that creates that image at the operator repo?
**Chris Lightfoot-Wild** 36:45 I don't think they want the workflow to have to build it and maintain it that way.
**Sergey Kleyman** 36:49 So, this is what I'm trying to understand. So, they don't want the workflow for PHP to be there, so…
**Jerry Ting Fung Leung** 36:55 You don't want the…
**Sergey Kleyman** 36:56 Thank you.
**Jerry Ting Fung Leung** 36:57 Yeah, they actually don't want the PHP code there, so they… so they want this folder, out of this PR, so that's what…
**Sergey Kleyman** 37:07 But all your changes to Go code, they're okay with it, because it's required to be there, right? Changes that will be able to pull the PHP container into the operator.
**Jerry Ting Fung Leung** 37:19 Yeah, they, they, they, yeah.
they're happy to… to pull the auto-instrumentation So, from… from other place, but not… not putting this directory into that place.
And, yeah.
**Sergey Kleyman** 37:36 Okay, so you want, then, the new repo to host both the code that is PHP specific, that will build the image, and the image itself, and also on the Docker Hub.
**Jerry Ting Fung Leung** 37:46 Oh, dear.
**Sergey Kleyman** 37:47 Okay.
**Bob Strecansky** 37:48 Sounds like it.
**Sergey Kleyman** 37:49 Yep, please go ahead.
**Bob Strecansky** 37:51 I was gonna say it sounds like a good case for an OpenTelemetry community issue to… get out the necessary things, like a new repo, and Docker Hub, and… Well, I guess GHGS, the GitHub version is, that comes with the new repository, but yeah, sounds like that… I think that's the right way to go, is open that community issue. Tag Trask, because like you said, I think he's one of the important people. I'm happy to introduce you to him, too, Jerry, if you haven't spoken with him before.
**Chris Lightfoot-Wild** 38:24 I mean, there is… there's Terraform to create these repos ourselves. Is that not intended for us to do just a PR for, or do you still have to… To the community issue first.
**Bob Strecansky** 38:35 I think they do the community issue for audit… like, for auditing purposes, but I'm not 100% certain. I just know that whenever I… whenever they talk about that in the, maintainers meeting, it's just, like, open an issue for… in the community. I think they're… I think they're actively working towards being a little bit more self-serve, but… I don't know that they're there quite yet.
**Chris Lightfoot-Wild** 38:56 It's only if there's reluctance, like, I don't mind, or I'm sure we can do it between us, like, doing that, change, and then saying, hey, we've got the work, please just accept, and then we'll be happy to get on with what we're doing.
**Bob Strecansky** 39:11 Yeah.
**Chris Lightfoot-Wild** 39:11 Mmm.
Cool.
**Bob Strecansky** 39:18 Does that answer all your… does that answer all your questions here, or do you have any additional questions about that?
**Jerry Ting Fung Leung** 39:23 I think, yeah, that answers the question, yeah.
**Bob Strecansky** 39:28 Wonderful.
**Jerry Ting Fung Leung** 39:29 Thank you. Thank you for helping.
**Sergey Kleyman** 39:32 Fixing up that, that work.
**Bob Strecansky** 39:34 Yeah.
**Sergey Kleyman** 39:35 Really good, thank you.
**Jerry Ting Fung Leung** 39:37 Thanks.
**Bob Strecansky** 39:39 Would you mind stop… just stopping sharing so I can share things?
**Jerry Ting Fung Leung** 39:43 shocked.
**Bob Strecansky** 39:46 Bye.
Alright, Paw a composer audit.
**Pawel Filipczak** 39:52 Yes, yes, so… We got a report from the SNCC. You remember there was some vulnerabilities, issues before, and last time we got also a report from the Elastic CA workflow.
And I started to dig, is it possible to include it for free in the OpenTelemetry repositories? And I found that the Composer has an option, or tool, which is called Odit.
And you can just call it, and you can scan for the log files, and also for the… it can scan live the handle for the vulnerabilities and the issues in the packages.
So it's just one command, it's Composer audit, and and it works, so it's showing the… the… issues, so we can scan during the build or testing, we can just call the composer.
To scan for the vulnerabilities, and it can show us that there are some… or the… our packages are, depending, dependent on the On the… on the other packages with… with the issues.
And we can try to update them, so it can be helpful.
for the… because in the distro, we are… we are packaging the… the… all of the dependencies together into the Debian or LPM packages.
So, it's very important to do scanning.
And in our case, in the district case, it will break the build, but for the other, for example, country packages, which are Some of them are abandoned, so we can just, you know, get the reports that they are, depending on the… on the outdated packages, and maybe we can just, you know, simplify… or just trigger some action from that.
**Bob Strecansky** 41:50 What's the VIN diagram of, like, this and, Renovate?
Or is there no overlap at all?
**Pawel Filipczak** 41:58 Yep.
**Bob Strecansky** 42:00 That was a question.
**Pawel Filipczak** 42:02 Yeah, but I'm not sure if Renovate can scan all of the packages, so… I guess it should do that, so… it depends what's… how the Composer JSON is…
**Sergey Kleyman** 42:16 No, it only scans direct dependencies that you mentioned in your Composer JSON. It doesn't scan transitive dependencies.
**Pawel Filipczak** 42:23 Yes, I think so.
**Sergey Kleyman** 42:25 And Audi does, it will scan your log file, so the advantage is, if you have security vulnerability in your transitory dependencies, Renovate doesn't know about it.
Like, maybe indirectly, like, if you… maybe, like, your direct dependency will become aware, right, because they will run right away, then they will probably release the next version that excludes those, even if just, you know, changing their dependencies. Then, you know, so you need your vendor, whom you take the direct dependencies.
they need to run Renovate, and then… then Renovate will be able to tell you that now you need to upgrade, right? You see? So you… Renovate directly cannot help you with that, only if you…
**Bob Strecansky** 43:09 Oh, yeah.
**Pawel Filipczak** 43:10 Yeah, renovate is not resolving all of the sub-dependencies in the trip.
**Bob Strecansky** 43:16 Understood.
**Sergey Kleyman** 43:19 Meetings?
But, Paw Yu, we probably want somehow to also run… see if we can run it on the other repos in OpenTeleen, right?
**Pawel Filipczak** 43:26 I guess we can do that. I guess we can do that. For example, if you are testing, building the country packages, SDK packages, then we can scan the full log files and the full vendor folder.
So… In that case, we can just get some notification that we are… Depending on, or some other behaviors are depending on… But the.
**Sergey Kleyman** 43:49 But this is exactly what then I… now I understand Bob's question. But your… but you… but then, in this use case.
Since your dependencies, they are dependent on your direct dependencies, right? So, Renovate would have found it. Like, so whatever Renovate didn't recommend, like, Audit will not help with that. Like, maybe it will just stress that now you are in a really bad situation, where one of your transitory dependencies is now a security vulnerability, potentially.
But until those vendors… let's say you're using Gazel as direct dependency. Gazel by itself maybe doesn't have any scrutinible bills, but maybe its dependency has, right? Let's say Coral.
**Pawel Filipczak** 44:27 And, and thrilled that.
**Sergey Kleyman** 44:28 The problem is that until Gazel team releases new version of Gazel that excludes that security vulnerability of coral, there's not much we can do, so this audit that we… it will intersect with Renovate, right?
**Pawel Filipczak** 44:40 It's not really that you can do, because the previous version may be not affected.
So you can just, you know, pinpoint the older version, so it depends. Sometimes the new versions are, you know, introducing some problems, some issues, right?
**Sergey Kleyman** 44:57 Right. No, I'm trying to go back to Bob's question, like, how is it… how is it… what is the additional value that it will get in addition to renovation?
**Pawel Filipczak** 45:06 So, for example, if you cook Gazzle, and Gazzle requires package… Let's call it…
**Sergey Kleyman** 45:12 Let's say total.
**Pawel Filipczak** 45:14 carrier, for example, carrier. So you can just pinpoint directly the carrier in different version, or updated version. So, carrier might be updated sooner than the Gaza itself.
**Sergey Kleyman** 45:23 You're saying let's, let's kind of, like, go over the head of the Gazel team, and pin, at least for some time being, let's pin it to the version without security compute, and then Gazel will reuse it?
**Pawel Filipczak** 45:34 Yes.
Yes.
**Sergey Kleyman** 45:35 Okay.
**Bob Strecansky** 45:36 So it handles transitive dependencies, is what you're saying?
**Sergey Kleyman** 45:39 Yeah, essentially, you will go and pull trans dependencies in your own composer.js and pin it forcefully into the version that is not… doesn't have the security mobility, just to force Gazel to also use that version.
**Bob Strecansky** 45:51 Understood, got it.
**Sergey Kleyman** 45:53 Yeah, I guess that might be an interesting use case.
Yeah, but there will be, you are right, there will be, like, some intersection between renovate and this. I guess it also might be, will give you additional, kind of, like, understanding, like, renovate just suggests stuff.
if this stuff shows you that now you need to do it because there are security vulnerabilities, right? And not just a regular update that Renovate suggests, because I don't know, when Renovate suggests something, does it show, like, if it's because of the security vulnerability or not?
**Pawel Filipczak** 46:24 Yes, it's showing, it's showing.
**Sergey Kleyman** 46:25 I'd chosen? Okay, so I guess maybe, in that sense, it doesn't add that, yeah.
**Chris Lightfoot-Wild** 46:33 Is this… it looks like it could probably work in contrab as well, does it?
**Pawel Filipczak** 46:39 Sorry, I didn't understand the question.
**Chris Lightfoot-Wild** 46:41 This could probably be added into Contrib as well, I guess, with the audit.
**Bob Strecansky** 46:47 And probably main instrumentation, too, I would guess.
**Chris Lightfoot-Wild** 46:52 I wonder what happens then in that scenario where you said, like, you decide to jump guzzle and paint the version of Curl.
if then Guzzle later on fixes their dependency chain, does audit tell you you can now drop your PIN for it? Because it's, it's fixed now.
**Pawel Filipczak** 47:10 then I guess you should do it manually. There is no way to, you know, to…
**Sergey Kleyman** 47:15 Well, I guess you can always go and, you know, like, try to deal with this separately. You can obviously automate it, right?
**Chris Lightfoot-Wild** 47:23 I don't know if, like, Composer Audit had, like, a prune command or something where you can, you know, just… It can clean up after itself if it…
**Sergey Kleyman** 47:29 Right, so essentially you're saying, please run audit as if we didn't pin it, and if there are no issues, please remove all this pinned stuff, because we don't need it anymore, right?
**Chris Lightfoot-Wild** 47:38 Yeah.
**Sergey Kleyman** 47:39 So you can do it, I guess, you will just need to make this tool a little bit more sophisticated, so it will be able to go and find out whatever you pinned, right, because then you need to be able to distinguish whatever you took dependency…
**Chris Lightfoot-Wild** 47:50 Unless this one that you've done here, just, like, native Composer Audit, like, if it has that functionality. I guess I'll just have to look and see if that's a thing or not, but… It's fine if it… obviously, if it gets you around security vulnerabilities, and you've got a means of seeing But it's fixed. That's fine.
**Sergey Kleyman** 48:09 Right, but this tool needs to… if you want to use this tool, so it will automatically… first of all, this tool is read-only, right? It doesn't try to make changes.
If you want this to be extended to the fact that it will automatically create PR and say, okay, let's spin it, or let's unpin it, right? So it's a little bit more… more sophisticated, scenarios that we are talking about, right? This is only for signaling. It will signal that you have issue.
But it will not actively try to resolve it in any way, or… Try to, you know, to remove the already stale resolution that was previously applied.
Other things can be thought about.
A little bit more advanced use cases, yeah.
**Chris Lightfoot-Wild** 48:54 Thanks for that, that's cool.
**Bob Strecansky** 48:58 Nope.
Alright, do we have anything else on the agenda today?
No, that's it. Should we walk through the PRs real quick?
Slightly.
A couple renovate ones here… go through… I have to go through… it's this.
Okay, okay, push it through that.
Contrive, have a couple… Circuit split.
Sergey, did you want to talk through this HTTP async line instrumentation?
Or this co-instrumentation.
**Sergey Kleyman** 49:50 I kind of, like, so… Yeah, so essentially, the PRs themselves should be simple in the sense that there were official options added to support capturing headers for the HTTP clients.
And I just wanted to add the support for those options. We already had support for, specific to PHP options and QRL, and I added, new names there, we still kept the legacy name.
And I added new names, but my problem with other packages is that there are no tests that test this functionality.
So, I guess I will need, like, if I don't want, because I… obviously, my concern is that maybe I broke the functionality itself by just saying the changes themselves are really simple, but who knows? So, I just need to add the… Just need to add some tests. And I'm not even sure how to exactly use… are you guys familiar with this technology, this HTTPS client?
like, I remember I tried to use it, but I couldn't construct a simple application that would invoke this kind of, like, functionality.
**Chris Lightfoot-Wild** 51:05 Don't use that package.
**Sergey Kleyman** 51:07 they only capture one, like, if you look at that, whatever, they only try to instrument one method, I think, SYNC, send or something?
If you look at that file… It's.
**Chris Lightfoot-Wild** 51:23 I mean, presumably you could mock it anyway, in a test.
**Sergey Kleyman** 51:28 Yeah, but, you know, doing tests on mocks, it's kind of like…
**Pawel Filipczak** 51:32 Samplex application with…
**Sergey Kleyman** 51:35 Do you have something? Okay, okay. Okay. So, but I do not… but I need you guys, I don't know if you already did, maybe, for CURL. CURL does have, tests, so that PR, it can be reviewed, that one is ready.
Interesting.
**Bob Strecansky** 51:51 No.
**Sergey Kleyman** 51:51 Yeah, so if you guys have some time to…
**Pawel Filipczak** 51:54 the option names, then you should also update the README. I guess. Oh, you did it for Carol. I'm not sure if it's a way for the…
**Sergey Kleyman** 52:02 Maybe I… yes, you're right, I will update the README for the ICMP. It has a README, yeah. It doesn't mention the option, but it mentions the INI option, so I will add the environment variable as well.
**Chris Lightfoot-Wild** 52:13 I couldn't actually see… I did a brief look at that. Where did you get that environment variable name from? Like, I searched the org, and it wasn't in semantic conventions or,
**Sergey Kleyman** 52:24 I took it from Java documentation. Yes, it's a good point where this.
**Chris Lightfoot-Wild** 52:28 I did… I saw a match in Java as well, but I didn't know, is that, like, the de facto one then, or…
**Sergey Kleyman** 52:34 That's a good point. Where do we have options documented? Should they be… usually they all come from… some of the options, I guess not all. They come from the SDK. SDK has some files with all the names, right? For the options.
But, are they… all of them should be there? Like, and you're right, like, is that taken originally from semantic conventions? Like, options being covered by semantic conventions as well?
**Bob Strecansky** 52:58 I think that one of the… not problems, but one of the things that we have to recognize is Java is, like, the… Trailblazer for a lot of these things, so they… they often will add new stuff before it's in the spec, or they'll do, like, tests or whatever, so I would be… Weary if it wasn't in the, specification, or if it wasn't in the, semantic conventions, but, yeah, I mean, that might just be worth a Slack search for that particular string, just to see if, like, where it came from and how it went.
**Sergey Kleyman** 53:31 Okay, I'll be all around.
**Chris Lightfoot-Wild** 53:32 That'd be great, yeah.
**Sergey Kleyman** 53:33 Yeah, I will link up whatever I find in the issues, that's a good point, yeah. It's definitely not Java only, I think Python is… I've also implemented that, but I will try to find the authoritative source, yeah, that's a good point.
**Bob Strecansky** 53:49 Thank you, Sergey. Feel free to ping us when those are ready, and we'll review them for you.
**Sergey Kleyman** 53:53 Thank you.
**Bob Strecansky** 53:57 I read this… Instrumentation… requirements… So I'll just renovate…
**Chris Lightfoot-Wild** 54:06 Well, Bob, I did approve your,
**Bob Strecansky** 54:08 Oh, nice. Excellent.
**Chris Lightfoot-Wild** 54:10 Thank you.
**Bob Strecansky** 54:11 Yeah, you do. Alright.
Just wouldn't.
**Chris Lightfoot-Wild** 54:16 And so did, Pawel as well, even before me, I was a bit slow.
**Bob Strecansky** 54:21 Facts.
Alright, so, emptying the disher… Oh, there's an issues tab here, too.
So, that's the dashboard issues.
Looks like there's just a couple little thingies, but nothing crazy.
About 44 million, so… which is exciting.
Alright, I think that's about it for this. Does anybody else have anything they'd like to discuss today?
**Chris Lightfoot-Wild** 54:50 for me.
**Jerry Ting Fung Leung** 54:51 Yeah, can I, can I raise one thing? Because… Sure. I, I put the link into the document, the PR.
**Bob Strecansky** 54:59 Oh, sure.
**Jerry Ting Fung Leung** 54:59 upon trip.
**Bob Strecansky** 55:02 Oh, I see it. I can… sorry, I can share it again.
**Jerry Ting Fung Leung** 55:04 Yeah, that one is about the SQL commenter thing that I worked before, and someone pointed out there's a bug in, the appending the query, so some… for some binary, so it… it can, corrupt some… with some binary, so, actually, it is a fix to… to fix that… that thing. And I… I also look at the… the PR, it should… it should fix the bug, so I… I think it should be good to go. Just… just see if the community has other concerns, yeah.
**Bob Strecansky** 55:42 Chris, I saw you started reviewing this. Did you have opinions?
**Chris Lightfoot-Wild** 55:45 Yeah, I can… I can have a look and, measure it, and if it's all good. Thanks for looking at that, Jerry. I think I did, tag you on it, Yeah.
Yeah, I also didn't know if you wanted to be… Sorry.
**Jerry Ting Fung Leung** 55:58 Yeah, because, when I first developed this feature, I… I didn't try on, other literal… binary… binary literal, so that's why I don't… I'm not aware of it, but someone pointed out, yeah, that.
Yeah, that's Hapaka, yeah.
**Chris Lightfoot-Wild** 56:18 I was gonna say about the code owners thing again, it just reminded me of that, spoke about it in the past, and maybe I should try and get around to it sooner, but it was more like the thought that I reached out to you because you'd authored it initially, and I thought, we've got no other automated mechanism of, like, letting you know that someone's trying to change it, obviously.
So that'd be cool if we got down the line and maybe, you know, be interested, or a vested interest in this particular instrumentation.
That you could be a code owner for it, essentially.
Without asking too much of you.
What was it?
**Bob Strecansky** 56:59 Alright.
Thanks, y'all, we'll see y'all next week.
**Chris Lightfoot-Wild** 57:03 See ya.
