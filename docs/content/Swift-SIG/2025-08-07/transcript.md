SIG: Swift SIG
Date: 2025-08-07
Duration: 92 minutes
============================================================

## Zoom Recording Transcript

**nacho** 00:42 Hi Bryce.
**Bryce Buchanan** 00:44 Hey, Nacho! How's your vacation going.
**nacho** 00:47 Hi, it's going. Well, yeah.
**Bryce Buchanan** 00:49 For good thanks for dropping in.
Oh, hmm!
**Vinod Vydier** 01:18 The other one. He came up.
**Ari Demarco** 02:06 Nope.
**Bryce Buchanan** 02:09 Hey! There!
**Ari Demarco** 02:12 And are you all.
**Bryce Buchanan** 02:22 Good! How are you doing.
**Ari Demarco** 02:24 Not too bad.
**Bryce Buchanan** 04:33 Alright. Let's let's get started.
So topics from last week are the data compression issue.
**Ari Demarco** 04:44 Yeah, follow up to you.
Yeah. Yeah. So I did a bit of research. The topic. 1st of all, the owner of the data compression merged the other pr.
but if you see the discussion that is linked on that other Pr, basically, he doesn't have a Mac with an m. 1 chip or higher to be able to do the coco pots push to trunk because he needs to have an m. 1 chip to do the vision. OS push.
So I suggested creating this gift card action that you can see in that. Pr.
so maybe you can all I thumbs up there. But that being said, I also investigated. If there's a native way on doing the Gc. And deflate that we are using in open telemetry.
There's no native way aside, of of the one that this repository is doing like there's no drop in tool like Gzip A and the other repositories that are out there, that has this implementation of Gc. And deflate. They also don't support cocoa pods or support only newer versions or stuff like that. So we are on the same problem.
So I think the the options are merging this Pr and eventually use that connection, because we depend on on the owner of merging the Pr. And also adding the secret or the other option is to copy only the Gcp. And deflate functions.
They are only being used in Otlp, Http export based module in just one file.
So maybe we can just copy paste it in that file.
in in the past. Probably we wanted to have an specific data compression model, so they that was going to be useful for other parts of the repo. But at this point I think it's not necessary at all, since that no other part of the repo is using it and thinking about it in that way is what actually caused problems in the past.
**Bryce Buchanan** 06:57 Right, right.
**Ari Demarco** 06:59 So that's it.
**Bryce Buchanan** 07:01 Cool. I guess. Let's try to get this worked out. And if that doesn't work, then I guess we can pull in those specific functions into our repo, so that.
**nacho** 07:14 30.
**Ari Demarco** 07:15 Yep.
**nacho** 07:16 So, yeah, yeah, yes. So I did last week. I've seen they updated the library to support vision in the package. And and yeah, I have merged up here with that update but the thing is that it doesn't support both cocoa pots right with.
**Ari Demarco** 07:36 And yet he couldn't do the push like, the marriage was was done like the pod. Spec now has vision OS, and all the stuff. However, he he couldn't push the pod spec to production. That's why I created the action so he doesn't have to have an m. 1, Mac to do it.
**nacho** 07:54 Okay.
**Alex Cohen** 07:55 He did mention, though in in your pr, or when he when he when he merged the original Pr, that he would be able to do it within a week or so.
**Ari Demarco** 08:07 Yeah, yeah. But I don't know. To make things easier is I just made that for him. So you can just when I click like do the the automatic push to cocoa pots.
and it also the the workflow I made also uses tags. So whenever whenever he creates the Spm tag it will automatically, automatically try to push that to to cocobots.
**Alex Cohen** 08:35 Yeah, I I totally understand what your Pr does. I'm just just saying that he said he would take care of it for us within within a week. So have we pinged him to see maybe he forgot. Maybe he got busy. So maybe we should ping him to get him to just do it.
**nacho** 08:52 Yeah, with this topic, we already we initially had this copied in our project because it didn't have as spm support in that library. Initially.
**Ari Demarco** 09:03 And we had that copied in the exporter only. But I think that after that we.
**nacho** 09:09 Extracted it to a library, because there were 2 users so there were 2 libraries, 2 of our targets or libraries that we build that linked with it.
And you say that now that there is only one you said that.
**Ari Demarco** 09:28 Yeah, yeah, there's only one Otlp, Http based exporter, I think, and obviously a test of that of that of that simple file.
But those are the only 2 files using it.
Basically, the one that actually needs it is the is the actual code, like, not the test.
**Alex Cohen** 09:53 So these are all things that we did like 3 weeks ago.
Right? This is not. This is not years back or far back. This is just a few a few weeks ago, so it's all pretty fresh, right.
We were all we were all there.
**Ari Demarco** 10:09 Yeah, yeah, I I just realized that while while I was looking at which functions we were using from data compression like the module, I found out that the only tool that we've been using is deflate and Gcp. And both of them just in that single file is is basically what I found, maybe in the past it was being used by other files. When we removed the dependency, the fork we had internally, or the copy, the copy module we had internally, there were more than one file using it, but as of now.
there's only one file using it.
**nacho** 10:46 Yeah, I'm yeah, yeah, I think we we we could. Also, I think Apple has a compression library also that you can manually call at least for deflate and for Gcp, it's just adding the header. But yeah, I don't think we should update that. But yeah, if we are only using in one place, I would say.
just take those files because they have an Apache compatible library. So if you copy those files into our project with yeah. And and only in that target, we we can.
Yeah, we can simplify for the future.
**Alex Cohen** 11:31 Also want to mention that the new topic that I put in which is not a new topic for everyone here. But that would simplify the complexity that we're having with making this decision a lot because it's moved out of it would be moved totally out of the main repository?
No, because it has nothing to do with the Api or the SDK, it's just one like another. A library that uses it for the Http request, or something like that. So at that point, it's a lot less important and can just be, you know, doesn't even need to be a dependency or not, and doesn't matter as much if something doesn't compile as well, because at that point it's it's not what everyone uses. It's just an extra piece.
but we'll get there, I guess.
**Bryce Buchanan** 12:22 Yeah.
Okay.
So I guess just for now, let's let's try to get that data compression. Pr merged. And we'll we'll worry about pulling in those other libraries. I I do see this apple z lib deflate available. So we could look into that if we need to. But let's leave that for another time. So, continuing on with the review of last week's topics, I haven't been able to make a pr for the the swift Ui view conflict yet.
I'm thinking that we're not gonna be able to wrap this in any sort of struct. So we're probably gonna have to rename it to like.
you know, hotel view, or something like that.
**nacho** 13:13 Yeah, I mean, we could add it as a child of another.
And but we will also have to recreate with it with a parent name. So I think the best thing the best thing we can do with that is renaming that.
**Bryce Buchanan** 13:32 Yeah.
**nacho** 13:33 And and use metric view for everything, and avoid any kind of conflicts in the future. Also because it's gonna it could be a nightmare, right? I don't know. Why would you put your Ui code directly with open hotel? But yeah, we we that's not the reason we should keep the name.
So yeah, let's I think, let's rename that.
And yeah, with that change.
yeah, think about the version. 2. I think that will need to be in the final version. 2 of the library.
**Alex Cohen** 14:14 Sorry I I missed the reason why we couldn't namespace it in a in a structor in other class.
**nacho** 14:21 There are no namespace themselves like in Swift. Directly you have to make that subclass of another.
**Alex Cohen** 14:35 Not sub, not a subclass just within the within. Another structure, or within another class.
**nacho** 14:41 Yeah. So that's a subclass right? Even if it's public, it's a subclass.
**Alex Cohen** 14:46 It's not a sub. That's not a subclass.
**nacho** 14:48 I didn't know.
**Alex Cohen** 14:49 Be an empty struct called metrics, and in that you put a struct you put this view struct you, you would be namespacing it into the metric struct. And you would do metrics dot view so to to create it or or to use it. That would not be a subclass that would just basically be an equivalent to a namespace.
It's not called the namespace, but it would be an equivalent.
So I was asking why.
**nacho** 15:15 But okay, yeah, I'm I think we we should rename it right?
**Bryce Buchanan** 15:19 Sure, yeah, yeah, either way. Just haven't gotten around doing that.
**Alex Cohen** 15:23 Well, I don't. I don't want to to. I'm asking why I'm asking what the decision is based on. This is. This is something that's that was brought up and like is important for this kind of thing. It's naming is important. So I think I'm just curious why we choose not to do the the within another struct versus just renaming it. Is it just a decision on the fly? Because we think that's the right way to do it? Or is there a reason.
**nacho** 15:52 Doesn't matter. I'm just curious.
Yeah, it's because it's way simpler for the users not having to always use a subname or mixing if you mix it with other, it's gonna create problems. We we want to make it as simple as possible.
**Alex Cohen** 16:10 Okay, I'm I'm actually one of the users that brought it up. And I I think the other way is is true, I think, having a an extra name like that is is a bit is a bit odd.
So are there any other users that actually said something about. It would be difficult if it was namespaced.
**nacho** 16:42 No, I don't think so, but.
**Alex Cohen** 16:46 Okay. Well, like, I said, I was just curious what the reasoning behind it was.
**Vinod Vydier** 16:49 Because he's he's at the group.
**Bryce Buchanan** 16:57 it was just an offhand comment on my part. I just haven't gotten around to try it out so I'll see how it works. And we can. We can wrap it in a struct you know, metric dot view. And see how that works right.
**nacho** 17:17 We are not so we we shouldn't do that.
**Bryce Buchanan** 17:20 You don't wanna do that.
**nacho** 17:21 All our classes are 1st Level classes. We are not supplacing or using anything like that. And it's not this the way swift works. You can always use the model name on top before if you want, but that's not the way that.
Actually classes work.
**Bryce Buchanan** 17:42 Yeah, it. It would be a departure from everything.
**nacho** 17:45 I, we shouldn't use a a naming convention. That is not the the standard.
So yeah.
**Vinod Vydier** 17:52 I think more descriptive does not harm right. It's only interested. Extra additional description of the name right? So.
**Bryce Buchanan** 18:03 Yeah, so should we, should we call it a metric view or something else? Then.
**nacho** 18:12 Yeah, I think metric view works well, or any other prefix that works.
**Vinod Vydier** 18:19 Metric view. Simple. And yeah, who's see?
Even if it's metric dot metric view, it would be, you know, reemphasizing that it is a view of a metric.
**Bryce Buchanan** 18:35 Okay, alright.
I'll just. I'll rename it. Metric view, then, and then that will solve this conflict with the Ui views.
the swift Ui views.
Okay, alright, let's move on.
let's see. Metric warning.
is this from last week this is from us. Did we cover this? I don't recall covering this.
**Vinod Vydier** 19:12 Yeah, this is a long one night. Yeah.
**Ari Demarco** 19:15 I don't remember that one.
**Bryce Buchanan** 19:17 Is that? Did this get added mistakenly on last week's reviews or last week's topics, and and we just missed it.
**Ari Demarco** 19:29 Oh, that's that's what I mentioned around the difference between mobile and back end in open telemetry and all that stuff.
**Bryce Buchanan** 19:39 Oh, right? Right? Right? Right? Right? Right? Yep. Yeah. Oh, this. Oh, yeah. I recall this. Now. Yep, okay.
**Ari Demarco** 19:45 But there's no no action there.
**Bryce Buchanan** 19:48 Yeah, no action. Right? Yeah. Just a just a guidance against using metrics and web and mobile.
But that's yeah. That's for end users and stuff. So your your mileage may vary, as they say.
Alright, let's Let's go to the the new topics. Okay, so we want to talk about split repo api plus SDK versus contrib. This is your talk topic, Alex. So it sounds like you think that the data compression. Conflict can be solved by this.
**Alex Cohen** 20:28 Well, that that's not the reason I bring it up, though, I just, I just think that the data compression issue is bigger because people linking against or people that that need the SDK or the Api But not really data compression, but are using data compression somewhere else, or something like that end up in that in that problem because of that. And they don't really care about the modules that that actually use data compression. But they're stuck with it. So this would solve that. It wouldn't. It wouldn't fix the problem in itself. Anyone using anything and contribute anything else would still have the issue, but it would move it to a much lower priority. And we wouldn't spend like 3 or 4 meetings talking about it. We're just like, okay. This is something that needs to be fixed now. But the main reason I bring this up is, and I know it's been brought up in the past, and it's probably a sore spot for a lot of people, I think, based on the reading. I've done and I don't want to keep it in this this for sore spot. But one thing I noticed, and one thing that I've always had sort of an issue with is whenever I load it up. You get all of these swift dependencies and all these other dependencies right that are not actually used by the Api or the SDK at all right. And yes, we have fast computers and all that stuff. And when we're small companies or startups using it, it doesn't really matter. Because, like the automation and Cis and all that stuff like it's we're not spending a lot of time there. And it. It doesn't cost that much money. But when you get to larger companies that are actually using this. And they have metrics and and dashboards and all that over the time that it takes to to download the their repos and compile, and all of that stuff, it becomes a problem, and it can be a showstopper for companies about using hotel or not.
And like I've I I know this I worked at. I worked at Meta, and I worked at square, and Meta would just block things that that that downloaded too much stuff that wasn't needed, or whatever or like data dog does fork it off, and then not even talk to us at all, and just do their thing right. And then we end up with different versions in different places, and then conflicts between companies, because they're using the same thing. But like in in different ways. So basically because of that, I just opened it up today. And I was looking for a sort of a solution as like the Api and SDK on their own, have 0 dependencies right? There's absolutely nothing as dependencies. So it makes it super small, super easy to import, and for anyone to just use, and they'll never be conflicts because of that and maybe we could even say we try and keep it that way right. No dependencies on Api and SDK and dependencies only in another repo that has everything that will be depending on the Api and the SDK so and doing that it would obviously help embrace the the embrace company, the one that that I work for. Get what we want done data dog will probably be able to just come back to this, because they don't really care that much about about the rest. They care a little bit, but a little bit less so they'll be able to come back to the main repo and anyone else that might have in the past looked at it and said, Oh, no, I can't do this because of all of this, and never came to a sig or never, never mentioned the issue. They'll just be able to start using it, too. And like, it's not a very complicated split to do. It's not much more maintenance or anything like that. It's like everyone has worked on one repo or 2 repos, or 3 repos perfectly fine. I think most of the other platforms have a main repo, and then a repo for contributions. So I think we just been, we would just be like bringing ourselves up to par with everyone else and really making it easier for everyone. So that's my pitch and you know, obviously I work for for embrace, and it would be it would be great for us we'd be. We'd love it. But I think other companies would love it too. And it would be easier maintenance. And to make decisions over a bunch of things in the future, I think.
and I also. I would also be happy to to do it myself, to put a Pr up and and do the split. If someone creates the repo.
**Bryce Buchanan** 24:52 Sure. Yeah, I mean it it definitely. This is something that keeps coming up. And it's a common pattern in the rest of the hotel projects, and the main reason why we've kind of avoided. It is purely just a like when it's been me and Nacho generally working on this and not many others.
It just becomes kind of a a difficulty to to manage all that. But it seems like, you know, this project has become a lot more popular. There's more people contributing to it. Ari's joined you know, as a as a approver. So I'm a little less apprehensive about doing this, especially with your offer, Alex, to to split it out for us. That would be really cool.
I don't know. What do you think, Nacho? I know that you are not a fan of this.
**nacho** 25:39 There is another reason that also bring this la in. One only repo is because at least initially, spm was a nightmare to configure.
If you unlinking things so people ended, linking twice, linking 3 times, getting duplications. And and I don't know if you remember Bryce, at the beginning it was like a nightmare just supporting dynamic libraries. We we made everything static just because people was constantly having problems with that and having to reboot.
We'll bring more of that. That was also the reason we can move on. Probably spm now is better with that one of the things I think that it. It helps discovery, having everything like this.
At the beginning. Now, maybe it's not so necessary because we have better documentation.
can have the examples also in a different repo that will also simplify things.
We we can go with that change.
that, that. Yeah, that could be a possibility that the.
What I always say is that spms would then be downloading dependencies of the libraries you are not building, or you are not targeting.
That's something that initially 4 years ago should have fixed 4 years ago. Right? That's something that has been like that for so long. That that's crazy that skipped like that we've thought initially that that will eventually happen.
And it it has not. And it doesn't look like. So I mean, it's totally crazy that this work like this.
They have something that you can have your own index with the project. So you have a copy and you download that. But yeah, I don't know why they they don't like that.
So yeah, we can go with this. I don't mind.
it's gonna bring more work and compatibility changes, and whenever we change something it's gonna be a nightmare to change that in all the dependencies of the exporters and that stuff.
and we'll bring more work.
But yeah, I let them. I I don't know how we will force that to happen when one when anyone wants to bring a change to the SDK or Api Api. They should also fix whatever happens in the contributions, and that's something that we cannot handle ourselves.
**Bryce Buchanan** 28:42 Yeah.
**nacho** 28:43 So I don't know how to do that.
**Bryce Buchanan** 28:45 I think that we need to think about how we handle version changes. I would. I would like to see a lot of automation around it. Like, if there's a version release for the Api and SDK, I want the contrib to immediately, like either create a Pr or, you know, like a version, update to the to the package for those dependencies, and make sure that that gets brought in immediately. Additionally.
**nacho** 29:12 Example. Now you change metric view.
the name, and what happens with all the exporters? When did you synchronize that?
**Alex Cohen** 29:23 I, I just wanna mention that like where I I totally agree that it can bring up problems like this. But there are like this. This is something that lots of everyone has been doing for a very long time. Like it's not. It's not something new. It's not something rare, right.
**nacho** 29:39 But it brings a lot of work. That's that's the point. And.
**Alex Cohen** 29:43 Well.
I agree that it brings a lot of work. I think it actually forces us to make sure that our things are aligned correctly. So things don't break. So we we have actions. We we have Ci that make sure that any changes don't break everything else like I understand that it it involves. There. There are things involved, and it's not as easy as having all the code in the same little blob. But I mean, that's that's just par for the course. Right? That's that's how things work.
**nacho** 30:14 Yeah, that's true. But but brings out I'm like changing the metric view name. You change that here. And what happens with all the exporters that are in another repo. How do you align with that to commit that in the repo? And you have to take the commit? You have to update the commit that you are depending on the other.
because spm is not easy for that either. So that was the reason. If you want to change, okay. Probably things will take longer to be updated or be fixed, and we have to. If we move that we have to move to away to handle all, all of those task I changes
**Alex Cohen** 31:01 So, really.
**nacho** 31:02 Have different compatibilities. We we I mean that that's gonna be a nightmare. And and the contributions to the project are really low, extremely low from anyone. So.
**Alex Cohen** 31:22 Which is good.
It shouldn't be too much of a nightmare, since there's not too many contributions, so changes won't be be huge. And, anyway, can't we just put like any changes into the Api or SDK? Can't we just put something in Ci that doesn't let you land them if it breaks everything in contrib.
**Bryce Buchanan** 31:38 Well, here's the problem. It's a chicken or an egg thing, right? So if we if we do have something like that, how do we?
how do we release an Api and SDK, to be like? And like, yeah, yeah, here's the problem. So you need a, you need a solid version in swift package manager to do any sort of releases. So if we block releases from happening, if Contrib is broken, we can't update contrib with the new versions until there's a release. And so it's kind of like, you know, a a cross compatibility issue there. So I think I think the pattern might need to be like, we observe the changes that need to occur.
We don't necessarily block anything in the the root SDK for releasing. But you know, we need to be aware when Contrib is being broken and maybe have a release branch that's being worked on in contrib that can be released alongside the Api and SDK, when that occurs. So just it's like kind of a a management of a little bit more complicated management of of the 2 sdks when releases happen like that.
**Alex Cohen** 33:01 Yeah.
**Bryce Buchanan** 33:02 If that makes sense.
**Alex Cohen** 33:03 No, it does totally.
**Bryce Buchanan** 33:05 Well, okay.
yeah. So so like, I was saying, I think that we need a couple of things. So automatic dependency updates and the Contrib.
or at least like release dependency Prs that can get generated and then worked on in a new like release branch.
**Ari Demarco** 33:36 I can help on the automation side. I tend to do it a lot. So.
**Bryce Buchanan** 33:41 Nice and then the other thing is, what was I? What was it? What was it? Oh, we should have like a Ci checker. That just runs the contrib tests when we make contributions to the SDK.
**Ari Demarco** 34:04 What is that?
**Bryce Buchanan** 34:06 So like, just like, pull down the contrib repository. Run the tests, using the Api SDK changes and not necessarily block anything, but just allow us to to, you know, kind of.
**Ari Demarco** 34:22 We know know that we broke country, basically.
**Bryce Buchanan** 34:25 Yeah, exactly.
**Ari Demarco** 34:26 Any changes. I see. Okay, okay, finish that.
**nacho** 34:40 Yeah. And the burning is when you have to break it right?
**Bryce Buchanan** 34:46 Yeah, exactly.
**nacho** 34:47 Have a change that breaks everything, and you have to change in both ways.
Yeah,
**Bryce Buchanan** 34:54 I think I think the only way that we can really make this work is, if Contrib is the version in Contrib is only compatible with one version of the SDK. And Api.
**nacho** 35:07 So kept in sync with main in both sides, always.
**Bryce Buchanan** 35:15 Or at least the latest release.
**nacho** 35:19 I don't know if latest release is the way to work, or just.
**Bryce Buchanan** 35:24 Well, I.
**nacho** 35:24 In Maine.
**Bryce Buchanan** 35:26 Well and releasing at the same time definitely.
Yeah, yeah, the release will have to occur simultaneous, not simultaneously, but what you know like, we'll release a new contrib with a new release of the Api or SDK. But the thing is is that contrib the the package swift package in Contrib is going to be pointing at a specific Api SDK version.
cause they're they're those are, gonna be dependencies. And.
**nacho** 35:56 Yep, yeah, definitely.
**Bryce Buchanan** 35:57 Api and SDK are going to be dependencies and contrib so.
**Ari Demarco** 36:00 Yeah, they they should do. They should use an exact, either for a specific version or a revision. You want to remain.
**Bryce Buchanan** 36:09 Yep, exactly. Yeah.
Yeah. And so so it might not necessarily automatically update in contrib what? When there's an Api or SDK release because there will be breaking changes potentially. But we'll need to create a release in Contrib that that takes in those changes so that it works properly. Yeah.
But it can't just be like main, you know. It can't just be like the main branch for Contrib.
because then nobody would be able to actually release a contrib package to the app store.
**nacho** 36:52 Yeah, you always need a numbered version. In order to release. Yeah.
**Bryce Buchanan** 37:03 Alright cool.
Make it so.
**Alex Cohen** 37:13 So to to do this, someone will need to. We'll need to decide what the other repo is called.
and someone will need to create that repo.
**Bryce Buchanan** 37:23 Right.
**Alex Cohen** 37:24 That has that is, a maintainer or Bruger, or whoever.
**Bryce Buchanan** 37:28 I think I think that Aloita might be the one who needs or or somebody in the Gc. Needs to create the repo. I I think that it should probably just be The the current repo name like dash contrib. So open telemetry, swift contrib.
**Ari Demarco** 37:52 Yeah, I'll I'll I'll follow that pattern. It's.
**Bryce Buchanan** 37:55 Yeah.
**Ari Demarco** 37:55 Open telemetry technology, contribute.
**Bryce Buchanan** 38:00 Yeah.
**Alex Cohen** 38:01 And if if everyone agrees that I can do, I can do the split, I will put up a Pr basically in both both repos, the one that removes a lot of stuff from the base one and moves a lot to contribute.
**Bryce Buchanan** 38:16 Cool.
**nacho** 38:19 Yeah. Now, now, 1, 1 question about.
do we want to make this part of version 2, we have a pre release version 2, that we plan to add a pair of Prs I don't know what. Probably we should add that to the topics of version 2 release today.
but yeah, and think if this is a change big enough, also separating into separate repos in order to move it also in the 32 dot 0.
**Bryce Buchanan** 39:00 Yeah.
**nacho** 39:00 Because I think it's a breaking change.
**Bryce Buchanan** 39:03 Oh, yeah.
**Alex Cohen** 39:04 I don't think we can pull it off fast enough for 2 point. O, though, I think there there are. We're gonna there's gonna be a bit of testing. There's gonna be like this, the the the tools that that Ari will will help build. I don't.
I wouldn't want to delay 2 point O, too much.
I think there's there's a lot of good stuff in there, and we could just end up delaying it, for who knows how long. Stick to the stick, to the original plan, I think for 2 point oh, and move this to whatever whatever next thing we're allowed to to have.
**Bryce Buchanan** 39:39 Or whatever we can have. We have a couple of major releases in a in a short period, but.
**Alex Cohen** 39:43 Yeah, I mean, there's nothing, nothing wrong, nothing wrong with that. There, the numbers are just indicative of what we're doing with the code right?
**Bryce Buchanan** 39:51 Yep, yep, 100%. Yeah. So I have no problem with that. Let's not try to force this into 2 point. Oh.
**Ari Demarco** 39:59 Concealing that should be this.
All these changes should be on a specific new branch, like we started doing with 2 point. Oh.
**Bryce Buchanan** 40:12 Yeah, we can. We can have these on a on a separate side branch for that purpose.
And then when we're ready to call it, you know. You know. Ga, I guess then we can merge it into main, and then make that the 3 dot O or whatever we need to do.
**Ari Demarco** 40:38 Sounds, right.
**Bryce Buchanan** 40:45 Let's let's have that in like I don't know if what branch you want to name it, but I guess we could do. Either you know. A 3 dot o release branch, or contribute 3 dot o, or just a contrib branch.
**Ari Demarco** 41:09 Whatever Lalik speaks, it's okay. I think.
**Alex Cohen** 41:13 Yeah, if we're if we're we're heading for 3.0 for this, which looks like we are just pick 3.0. And even, if possible, make 3.0 like this.
Only this, yeah.
**Bryce Buchanan** 41:27 Yeah.
**Alex Cohen** 41:28 It's done for 3 point. Oh, and put it in a 3 point O branch, and just.
**Bryce Buchanan** 41:33 Focus on this.
Yeah, let's just let's just do 3 dot. Oh.
alright cool. Yeah, let's let's have that work be done in the 3 dot O branch on the on the SDK, or the yeah, the open telemetry. Swift repo.
**nacho** 42:00 Sorry I had a problem with a table that had may not.
**Bryce Buchanan** 42:07 Alright, I will.
I will follow up on getting that.
That repo created cool any other. Any other issues with this topic or any other new topics that we want to discuss.
**Alex Cohen** 42:36 I I just had a small idea regarding the view from that I wanted to mention. It's just an idea. If if it works for you guys, great for everyone, great, if not, it doesn't matter. But I was looking at what apple does with their their sub classes or sub, not a subclass, but within other class, within other struct and often they do that. But then they go outside of the struct and put a type, alias to the name that they want at the global. So we could put view within a metric struct so that would be metrics, dot view. And then outside of it, we could have a type, alias that is, metrics view equals metrics dot view. So you could use.
You could use metrics view like you want to, but also hide the the view, which is the actual spec name, I think, within the metric structure, so that we could have best of both worlds. I just know I was looking at. I was able to think of one place where Apple does it, and it's within notifications in Swift. So they have the notification.name, right? Which is which is basically they're all strings in objective C, but in Swift they're still strings, but they're still.
They're like the notification.name struct that that or you know, I guess it's a struct.
**Bryce Buchanan** 43:51 Oh, yeah.
**Alex Cohen** 43:52 The name of the class in, but it's actually notification.name. So name is within the notification structure. So, anyway, just just an idea if you wanted to look into that, if if that, if that helps at all.
like what Apple thinks is the right way to do it. So.
**Bryce Buchanan** 44:10 You said that was in the notifications.
**Alex Cohen** 44:13 Yeah, you can just go open up notification.name or notification center. It's all all in the same file, anyway.
**Bryce Buchanan** 44:21 Well, I'll take a look at that. Alright, let's do a quick review of issues since we have a couple more minutes okay. Still, there.
it looks like.
**nacho** 44:46 Yeah. Dude.
**Bryce Buchanan** 44:46 That's getting followed up on.
I can't remember.
Okay, that that's active. Right now, I'm just trying to remember what we all got assigned. Okay, yeah, Vinad.
**nacho** 45:03 I have.
**Bryce Buchanan** 45:04 Able to make.
**nacho** 45:04 Have answered some of these, yeah, not just earlier this week.
**Bryce Buchanan** 45:08 Supposed to be on vacation.
**nacho** 45:12 Yeah, but yeah, I am on vacation.
**Bryce Buchanan** 45:20 So is. Does anybody need any support on any of these, are they? It looks like.
**nacho** 45:25 Yeah, yeah, this one this one. I, I think this one comes from the you know, the asynchronous network methods that we instrument when they use an asynchronous method that doesn't have a delegate. We have to put ourselves a delegate in order to capture it.
**Bryce Buchanan** 45:46 Yes.
**nacho** 45:47 Yes. So then, when it uses the callback received response, that one in the asynchronous delegate method doesn't include any data, so you cannot get the data from the request.
So that that's the problem that yeah, that that he's having. So I I am asking him if it's because of an asynchronous task. And if he can provide that fake delegate and maybe with that real delegate, we can put that data inside. Because with our fake delegate.
We are not filling that information because it doesn't come in that method.
So it's a bit difficult to fill.
But just checking that. And that's that's the issue. I don't know if we in the fake delegate, or if we should use another delegate extra delegate, that, apart from from getting the the end, also recovering the data that comes from the network request.
So yeah, that's something that we could improve so just validated that it's an asynchronous task, the network request. And and I think that that's the issue.
**Bryce Buchanan** 47:14 Okay? I see.
Yeah, this this one's interesting because this feels like a new, a new issue. That has occurred the it seems like resume is getting called twice in the URL session instrumentation, which causes 2 spans to get created. Very unusual. I'm not really sure.
**nacho** 47:56 Yeah, that's I have also answered that the thing is that when you have to add headers to any request, you cannot add that to a already created request that comes to the network. So in in the case you have to inject your own headers, you have to create a new request based on the on the previous one. But you have to create a new one.
and it looks like the method that creates that request is called twice. I don't know why.
Release. Yeah.
**Ari Demarco** 48:30 I had to solve a crash similar in at embrace. And there's some people doing some kind of debounce logic with request, so they resume, then false, and they can resume again the same request.
So that's a thing that could happen.
So whenever you switch or resume, you had to check the actual initial state of it. I can give it a look if you guys want.
**nacho** 48:58 Yeah. He. He also mentions that he had. There is also a callback that says, shoot instrument.
So it provides you information in a callback, and and you decide, if you must instrument that network request. And he says that putting false the second time it it works as expected.
So I suspect that comes from probably asynchronous request that that's not following the flow we expect initially, and maybe it's and in the the the headers twice.
But yeah, you can take a look, Carrie, if you if you want.
I think it's because the the method is called twice here. But yeah, maybe if it's related to what you found, maybe it could be also that reason.
**Ari Demarco** 49:55 I can look it's it's weird, though, because in in the past that led to some crashes in our side. So maybe it's something different. But I'll take a look and see. Maybe it's it's similar.
**nacho** 50:07 Okay. Yeah. Great.
**Bryce Buchanan** 50:08 Thanks. Yeah, that'd be appreciated. Get your get your thoughts on it.
okay, cool.
Alright. I think that that covers it. Well.
**nacho** 50:33 Yeah, what about 2.0 release? Sorry?
**Bryce Buchanan** 50:37 Oh, yeah. So.
**nacho** 50:39 What, what things we must. I mean, we said, we will release by the 7th of August we released 2 weeks ago, just in pre release. Right? So.
**Bryce Buchanan** 50:48 Yeah, yeah.
**nacho** 50:49 So we more or less. But we had one pr, that was fixing an issue with network request. We ask for some tests. They don't appear, but it fixes a real issue.
I think that we could just merge it and maybe add the test in the future. So we have that thing fix for the 2.0, and also your metric view. Pr, I think that should come in.
and with that probably we can release what what do you think.
**Bryce Buchanan** 51:23 Those seem to be the the main things right now for the final release. Yeah.
**nacho** 51:30 So let's merge that Pr, even if the user didn't provide tests for that, because it already has no test. So it, it's not worse than it was before.
I and and and let's yeah, yeah, let's wait for your metric view and and let's release with that.
**Bryce Buchanan** 51:55 Yep, sounds good. I'll try to. I'll put the. I guess we have a meeting with Alita after this, but after that I'll I'll try to put that pr together as quickly as possible.
Cool.
**nacho** 52:07 Okay, yeah, I will be checking for for approving. And all that stuff.
**Bryce Buchanan** 52:11 Oh, okay, thanks. Thanks, Nacho.
Alright. I guess. That's it for today. Everybody have a good weekend. I'll see you all next week.
**Ari Demarco** 52:22 See y'all. Bye-bye.
**Bryce Buchanan** 52:24 Bye.
