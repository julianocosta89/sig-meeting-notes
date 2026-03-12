SIG: PHP SIG
Date: 2025-06-25
Duration: 40 minutes
Zoom Recording URL: https://zoom.us/rec/share/IXcE_HhfRIjYTXeHkPRK2QrT2A7NtHtu-nn76SosHw-XYvomlJ--tB43PhpUQrq1.2hBJ3lpAIK8PAGFB
============================================================

## Zoom Recording Transcript

**Sergey** 01:50 Who's old.
**Chris Lightfoot-Wild** 01:54 Hey, Sean, hey? So, okay, there, you guys, how's it going.
**Shawn Maddock** 02:03 Good.
**Sergey** 02:04 He had a car cut recently.
**Chris Lightfoot-Wild** 02:06 I did. Actually, the bugman is gone.
**Sergey** 02:12 I heard a mallet.
**Chris Lightfoot-Wild** 02:14 I didn't have a mother. I had like a little man bun thing, but over Covid it started growing, and then put it up behind here and forgot about it. And yeah, 5 years blipped by, excited to have a backup.
Oh, Brett and Bobber, it's okay.
**Shawn Maddock** 02:49 Bob just posted. He's running 5 min late.
**Chris Lightfoot-Wild** 02:52 Okay.
sorry. Just kick something over behind the desk.
**Sergey** 03:10 Yeah, usually Brett. It's always on time, right?
**Chris Lightfoot-Wild** 03:15 It looks like he's online.
Maybe it's having some issues close on slack. There he is.
Speak of the level.
**Shawn Maddock** 03:54 We're not.
**Chris Lightfoot-Wild** 04:01 Some issues.
**Sergey** 04:23 Oh, jinxed it! We lost bread.
**Chris Lightfoot-Wild** 04:38 See you now. Brett can't hear you, though probably.
**brett** 04:48 And about, now.
**Chris Lightfoot-Wild** 04:49 Oh, yeah, there you go!
**brett** 04:53 Sorry about that.
**Chris Lightfoot-Wild** 04:57 I thought all those audio issues were fixed as well for the time. There.
**brett** 05:01 Looks like I've had an update since then least I knew what buttons to mash.
Hello, Sergey, welcome back! It's been a couple of weeks since I've seen you.
**Sergey** 05:15 Yes, I don't know if you're following. We had some some issues in the area.
**brett** 05:22 Yeah.
**Chris Lightfoot-Wild** 05:29 I think you're okay.
**Sergey** 05:31 Like to wait for Bob.
**brett** 05:36 We could probably just start without him unless we're gonna make him drive. I'm not. So I don't have anything ready to maybe. Chris, are you able to screen share if you've got.
**Chris Lightfoot-Wild** 05:49 Yeah, I can.
**brett** 05:50 I haven't even looked at the agenda for today. Sorry.
**Chris Lightfoot-Wild** 05:55 Just bear with the second one. Sorry.
So thank you very much. Thank you.
Oops.
Awesome is all right.
You'll see that.
**brett** 06:34 I can see that.
**Chris Lightfoot-Wild** 06:36 Sweet.
Oh, hey, Bob, just Bob just moved. Bob, did you want to stay? We're just about to start.
**Bob Strecansky** 06:43 I can.
**Chris Lightfoot-Wild** 06:44 I'll let you be the driving force.
**Bob Strecansky** 06:47 Sure. No problem.
Sorry everyone about a half hour of traffic for a 10 mile drive.
You gotta love living in the big city. How's everybody doing today?
**Chris Lightfoot-Wild** 07:00 Good, that's it.
**Bob Strecansky** 07:02 And alright. It's reorganizing to not share corporate secrets.
Trigger. How's your time off.
**Sergey** 07:11 It goes quite nice visited couple of States, mostly Wisconsin, Montana, Utah.
**Bob Strecansky** 07:18 Oh, you did!
**Sergey** 07:19 That you did. You did special parts really like the rocky.
**Bob Strecansky** 07:23 It's concept you went like.
**Sergey** 07:25 I went from Las Vegas to Denver.
**Bob Strecansky** 07:27 Okay.
**Sergey** 07:28 Yeah.
**Bob Strecansky** 07:29 That's cool. It's the perfect time of the year to go on that kind of trip.
**Sergey** 07:33 Yeah, I mean, I was surprised. I expected more people that would.
**Bob Strecansky** 07:39 You know we're do. We're We're not as we're not as concentrated as most of Europe.
**Sergey** 07:46 Well, obviously, after Memorial Day, right? Those people started to to flood in. But yeah, it was better.
**Chris Lightfoot-Wild** 08:01 I want to visit Montana as well. I've been watching Yellowstone on TV that looks.
**Sergey** 08:07 I really recommend Rocky Rockies is also quite beautiful national Park.
Or, for example.
if you're into kind of like more deserty thing like in in Utah they have Zion quite also quite a beautiful national park.
**Chris Lightfoot-Wild** 08:23 Yeah.
**Bob Strecansky** 08:24 There's a lot of really interesting national parks that our current administration is trying to get rid of, but hopefully they won't alright. So say it again.
**Chris Lightfoot-Wild** 08:36 Make good golf courses. That's probably.
**Sergey** 08:38 Okay.
**Bob Strecansky** 08:39 As a competitive junior golfer, I can tell you that's true.
Alright. So do anybody have any walk on topics today for our agenda before I start rolling through our normal rigmarole.
**Sergey** 08:55 Pabel mentioned to me that you guys were discussing the work that we started on the Kubernetes operator. So if you have some time left. We can. I can describe the current status of it, and we can. Maybe if you want to see if we can push it forward.
**Bob Strecansky** 09:14 I think.
**Sergey** 09:15 We can do it after that.
Regular steps in.
**Bob Strecansky** 09:18 Oops that works for me.
Man, there's so many links to open now. I need to like set up a alright rework service info factory priorities. Brett.
**brett** 09:40 Yeah. So I think that's that's ready for for re-review.
That sort of yeah. Come out of a a bug that was raised.
It's only dude.
**Bob Strecansky** 09:54 Okay, I will review that.
So and then log for log record processor enable, I think we approve this one.
Yeah, this one got approved and looks like nibay, had a couple of things that he wanted to talk about.
**brett** 10:13 Okay. I better go back and look at that. I don't. I don't think I've addressed Nive's.
**Bob Strecansky** 10:20 Yeah, it looks like I think I think I approved it. And then he came back and gave a couple more things that he was talking about. So, okay, yeah, just just feel free to tag me when that one's ready.
**brett** 10:32 Very good.
**Bob Strecansky** 10:34 And I think that's all the open new stuff there.
Hmm, trib update community member listings.
Looks like right. You recommended some changes here. I saw I saw this this morning. I will take a look at that, too. That seems right. I have to change this. This is no longer Mailchimp I now work for into it.
which is something that I I often also forget. So don't feel bad about that.
This Pdo metrics, one I've been waffling back and forth on. Has any have any of the other approvers looked at this yet?
**brett** 11:19 A little bit. Actually, I started looking at metrics more generally today.
Just because I've been playing around with the hotel demo sort of for for my day job.
yes. So I'm hoping by trying to sort of implement some metrics in in one of the other things. I'll get a better understanding of what? What this Pr's sort of trying to do with the sort of generalized utility functions that that this author's trying to develop.
**Bob Strecansky** 11:57 Got. It sounds good, so we'll leave that for now. I mean, it seems like a relatively straightforward Pr, but I'm just always.
I'm always a little hesitant with new contributors that don't talk to us, and just like throw stuff into the ether. But that could also just be this person's way of working so alright back to it, I think.
The doctrine span link spread. Can we merge this one? I think it's been approved?
No, then it's.
**brett** 12:28 Is there anything.
**Bob Strecansky** 12:31 If there's anything blocking now, alright in it goes.
**brett** 12:35 Do it.
**Bob Strecansky** 12:40 Alright. I think that's about it. Here.
**Chris Lightfoot-Wild** 12:43 The the installer, one.
**Bob Strecansky** 12:46 Oh, sure!
There were changes requested for it!
**brett** 12:51 Yeah, I think we need to talk about that. We've we sort of talked about just generally a couple of weeks ago.
you know, just how do we sort of except.
you know, 3rd party thing. And what are your responsibilities? And yeah, I see this person's tagged me again just to for what's going on?
We haven't. Yeah. Well, sorry. What were you gonna ask, Chris, did you have anything specific to.
**Chris Lightfoot-Wild** 13:22 Well, no, I don't. I've seen.
I guess I'd interacted with this thread at some point, because I'd seen a notification that they were chasing, and I just wondered if I I didn't realize we were waiting on changes. Have they been dismissed, or can they be dismissed now?
**brett** 13:36 Know that we are waiting on changes. Oh, maybe it could just be a thing that needs to be a discussion that needs to be closed, but I think it's
**Bob Strecansky** 13:49 Is it a licensing thing.
**brett** 13:51 I think they've done that. I think that was that was a while ago.
Yeah. So so I think it's really just on us. Is there any sort of extra wording that we want to put on this for?
You know what what we do? If if sort of Ibm sort of maintain as a sort of, you know, non responsive if they abandon it.
you know, or what? What are our What are the expectations on on the open telemetry project for for maintaining this.
**Bob Strecansky** 14:28 Yeah, we're so was that last week that we talked about that like how we're we're talking about.
**brett** 14:34 Weeks ago. I do remember you did ask something in the Maintainers Channel.
**Sergey** 14:40 Do you know what other teams doing like, for example, Java? I know that they have quite an extensive contribut.
I don't think.
**Bob Strecansky** 14:49 Yeah, after we we talk, we've talked about it with some of the other Maintainers, and we talked about it in the Hotel Maintainers channel and didn't really get a lot of response. But I think, like the general rule of thumb is, these packages are like, quote, unquote, without support or whatever like. It is the onus of some of these companies to maintain these things, and if they stop working, then they stop working. We, as the open telemetry. Php. Sig. Are responsible for the Api and the SDK. Primarily, and these other packages are there is a responsibility of the companies and institutions that run them right like we don't. I don't have an instana instance that I can test. I don't want one right like, I'm not gonna use this. So I think it's like it's 1 of those things where we have to just focus mostly on the Api and SDK and give best effort where applicable for contrib packages. But there's no guarantee on contrib compat like contrib collaboration, because it's just too much. And you know, there are tens or hundreds or even thousands of custom integrations that you could do with us, and we can't put all of our effort into maintaining those things.
**Sergey** 15:59 So the the current kind of like best practices to even keep it in external repository, not even part of country.
**Bob Strecansky** 16:08 I think that is also a big point of contention, too. I think the I. The idea behind the contrib repo is to make it clear and concise and simple for companies to contribute to open telemetry and follow patterns and see what other people are doing and be collaborative. And all these things and make sure that the it's like publicly available, and has the same kind of scope as our Api and SDK. Repos. And same URL, for you know all of these things that become sort of important as you're trying to implement production software. But I think that there, there are definitely places where companies and institutions just go. We're gonna do it in our own repo. And that's fine, too. I think it's just
**Sergey** 16:50 So you're saying, it depends on the company company can can put it in country or choose. It's it's up to them.
**Bob Strecansky** 16:57 Yeah, I mean, there's nothing.
**Sergey** 16:58 No, but it's fine with us as a as an open telemetry to allow them to keep it in country.
even though, like you said, they can abandon it at some point.
**Bob Strecansky** 17:07 Yeah, I think I don't. I don't love the fact that that they can keep it in contribut and abandon it. But I mean that could happen with anything like the guzzle.
**Sergey** 17:16 Yeah, that's why it brings kind brings the question, what's the difference between contribut and kind of like the main repo? Right?
Where the kind of like. What is the line of responsibility.
**Bob Strecansky** 17:27 I think we were. We were attempting to gain clarity on that, and I think we never like. I don't. I think it's ambiguous on purpose, which is frustrating. But that's just the state of open source software, right? Like, nobody wants to put us a line in the sand anywhere. So I think I think we just have to keep chugging along where we can, but don't put too much energy into contribute. I think it's important. I think it's important, but I don't think it's ever going to be urgent.
**Sergey** 17:54 But this is a bit tricky, because most of the good kind of meets meaty stuff isn't contribute at the moment. Right? All the instrumentations.
Yeah, so it's kind of.
**Bob Strecansky** 18:02 I agree with you.
**Sergey** 18:02 They say that contribut is not important.
**Bob Strecansky** 18:05 Yeah, I don't. I'm not saying that it's not important. It's very important. I think the important thing for us to focus on focus on is the Api and the SDK and the implementation strategy needs to get needs to get appropriate attention when we need, when it when it must happen.
**Sergey** 18:24 No, I guess for me the delineation would have been like, I guess.
like, what is the stuff that we worry? Yeah, I agree with you that Sdks Api is top top priority. And then but the question becomes some point like, Okay, if build fails, or whatever is that something that we can defer and address it in indefinite future? Or is it something we would like to address as soon as possible? Right? And then we can question becomes, okay. If this is the delineation point line right? How much of a priority it becomes. If something doesn't work, then maybe it's a good point of keep it in a pro in, you know, in separate repos, important stuff versus less important. But like you said that we can always change it in the future, right? Nobody currently depends where its limitations live, right? The ones that we kind of like take responsibility for.
**Bob Strecansky** 19:12 Yeah, that's.
**Sergey** 19:13 If I understand Java, for example, they do keep them in main, and they contribute. They only keep stuff that is less important. But I'm not 100 sure. I think I'm not sure like, what is the delineation like for Java between Contribut and the main repo.
**Bob Strecansky** 19:27 Yeah, I think again, I think it's 1 of those things right, like we have to do the best that we can with the resources that we have, and if we need to make changes in the way we operate in the future, that's fine.
I think we just have to keep rocking along sort of in the same way we happen.
**Sergey** 19:44 Sounds good.
**brett** 19:50 Yeah. So I think I sounds like the final call is, is We just play around with the wording of, you know, audio sort of responsibilities are which I think they've already made some changes that I I suggested.
and then accept it. And then it's it's best effort which, given that none of us have access to Instana or really care to have access, because it's really it's not open telemetry. It's just a it's an exporter for for a different product that's probably going to be.
There's not a lot that we can do if something breaks. So we we're gonna have to defer to to those developers and hope that they show up to fix bugs.
**Bob Strecansky** 20:43 This is something that.
Yeah, this is something that I am I. And I think a lot of other maintainers are worried about. Sorry the I don't want to call it a doomsday scenario, but like this scenario that you just talked about, I am, I put in a cool contribute package for into it, and then a thousand people rely on that package, and then I stop maintaining it. And then what do you do in that situation? Right? It's like those people are relying on that package to do to do their production workloads, and then nobody maintains it. And you sort of have like this shroud of responsibility that gets skirted because you have the like, our us, the Maintainers, and you have the contribute maintainers which are most likely different people and have different agendas. So again, we gotta just do the best that we can. Don't stress about it too much. And if we have to revisit how we handle these things. That's fine. But no, I wouldn't lose any sleep over it now.
**brett** 21:40 Yep.
**Bob Strecansky** 21:45 Alright. No instrumentation. Full requests.
No, I haven't seen this one.
**brett** 21:56 That's new.
**Bob Strecansky** 21:57 Yeah, I I could have sworn we've checked these.
Oh, you did! You responded to this, but.
**brett** 22:04 Oh, okay. Very good.
**Bob Strecansky** 22:06 Good work.
**brett** 22:07 Hang on.
It'll be very important if they haven't responded for.
**Bob Strecansky** 22:11 Yeah, probably anything on this project board. Anybody wants to talk about.
**brett** 22:23 Not me.
**Bob Strecansky** 22:27 That's the case. Still empty.
16 million insults bizarre.
Wow! 30 days we've had 1.5 million. That's pretty cool.
I'm curious. What are the Php versions looking like now?
They're growing alright.
That's it for normal agenda stuff.
Sergey, you want to talk through the Kubernetes operators.
**Sergey** 22:55 Right. So paul mentioned to me that in case maybe, I misunderstood him. So you wanted to see what is the? And I think the question was about documentation, but maybe status in general, so I can quickly describe, and we can see. I remember we had the we had somebody. Unfortunately, I forgot his name. I don't think it was Sean right? That was also expressed interest in this area.
he contributed a lot. Maybe Brad, you remember who I'm talking about? Maybe before I left for vacation couple of months ago, we had a guy that contributed a lot, and then he joined one of the meetings at least.
**Bob Strecansky** 23:33 Oh, Nick, it! Nick!
**Sergey** 23:40 He, he joined recently. I think you talk about Nick, Hugh. It was a long time ago, but doesn't matter. Maybe I remember later. So what in any case, the current status of it. And then we can see how we take it forward. So essentially, this Kubernetes operator, just to refresh everybody's memory what it's supposed to achieve this feature so essentially, it allows to inject this kind of like instrumentation without even changing. Not only so, you know that we have this elastic distribution. It's a target, not even force, not even require application developers to change the application configuration like in this case, Composer Json, but allow installing opentelemetry on the per site level, and then all the applications will be monitored by opentelemetry. But this Kubernetes thing takes it even step one step further, it says, Okay, not only that. I don't want to change the application. I don't even want to change my containers that involve this application. So I want to inject this this capability of instrumented application outside even the container.
So I keep all my, and in this case, Kubernetes, I keep all my pods as they are, but I don't want to change the differential containers. I only want to add this essentially markings on the pods that I think it's called attributes. So I don't remember labels. So you essentially mark your pods that you want to be monitored. And then this capability of this operator is to inject something. And in this case we're using capability of injecting environment variable. You can inject environment. This is what Kubernetes kind of like infrastructure allows you to do so, you can implement this operator that will check. If you have this label, put on your pod. Then in turn, you will inject environment variable you can.
This is what other languages do. And you can mount files right? So obviously, this environment variable will reference those files. So in case of Php, I ran some experiments. What we can do there is this environment variable called Php scan, or something. We can inject that environment variable by adding, pass where we will place any file that will mention our extension and the rest of the files that we need to be in order to inject right. So if we follow the same approach as we did for elastic distribution, we essentially injecting the extension. And we're using maybe kind of like ability to load the files, either maybe using preload or maybe implementing this additional feature of the extension of kind of like bootstrapping by calling into Php code. So this is this is still not settled. But we can. We can decide what to do there.
And essentially, we can achieve the same result that other languages achieve which is, you don't change the application, don't change the container, but still we have this extension being loaded, and all the instrumentations are being bootstrapped, and the application is being monitored. Right? Obviously, people will need to configure where to send the data. But that is the same as for the other languages. So currently, only the 1st part is implemented, and by 1st part I mean, we have all the possible combinations of so essentially the binary for the extension right? We need to build it for for all the architectures that we might support and all the possible lip. See variants right? Because you can have, like, for example, Linux on intel pro imd. But, for example, Alpine uses muscle and ubuntu uses gnu Lipsy, and they're not compatible, so you cannot use the same binary. You need to build separate binaries. So you have all these possible permutations of different architecture parameters. So we pre-built the binaries for them. And we essentially have a container that keeps all of these things inside of it.
And when this operator is invoked, so what the operator does, it needs to essentially select what binary to use and also based on Php version, it needs to select what? what to use for instrumentations, right? Because while maybe instrumentation themselves might not depend on Php version, but obviously the dependencies, the transit dependencies that they have might depend on Php version. So we essentially prepare the separate vendor directories for each Php version. So so what is missing currently so this part is already done, the one that generates all these permutations and keeps them together. What is missing is the implementation of this code that will run at the level, like what the part of this operator that will select, given it needs to be given, obviously, which Php version is be application is using at least at the moment. Right? We can maybe make it more user friendly later. But so given the Php version and the architecture it will select, which binaries to mount.
and then it will inject this environment variable that I mentioned. So it inside the container. Well, application will boots will run. It will automatically bootstrap everything.
So that's the status. Right? So essentially, there is no documentation so immediately to answer the question of the documentation. So the the goal was after everything is implemented. That also will include documentation that is essentially describes how this feature can be invoked.
which, like, I said eventually, for the user that means putting this label on their pods and where they know that they have Php applications running.
And this additional parameters that at the moment, if we cannot detect them automatically, we will have to require user to specify them manually. So like, for example, the Php version.
I remember we demoed in the past that in elastic we do have this load.
**Bob Strecansky** 29:43 He's.
**Sergey** 29:44 That can automatically detect Php version and load a binary. According to the detected version. I think we could do the same for the Php version as well for the, for the vendor part for the Php part of the so essentially for the instrumentations. So technically.
if if by the time we implement this operator. We already contributed our elastic code to to upstream. We can use those capabilities, but at the moment they're not there, so will require users to manually tell us which PC version is they want to monitor and I think maybe also they will have to tell us like what Lipsy library variant they have like. So essentially is it Alpine or boot, or whatever?
Maybe we can detect it. But I'm not sure, like I'm not technically 100%. If the this operator, the context that it's running in, if it can already know what this container is going to be with container, with the application. So maybe I saw, like, for example, other languages such as.net. They do require users to tell them what is gonna be like Lipsy or this muscle. So there are some technically technical things that maybe we can require users to specify manually the beginning. And then later, maybe we can find the ways to detect them automatically. But this whole part that does it is missing. So it needs to be implemented.
Like, I said, other languages already have it. So it's essentially taking look, taking a look at what other languages they're doing.
and mostly copying and adapting into Php use case.
Right? So that's that's the current status. So if somebody wants to sync up and work on it together, so currently, we kind of like from our point of view, put it a little bit on hold, because we wanted to 1st contribute. Like, I said, some of the features that will make it much simpler to implement this operator for Bhp upstream. But it's not like they must have the big upstream before we implement. We can do it in interleaved way.
So we just wanted to save ourselves effort for now. But if somebody wants to work on it now, it can be done even without waiting for the elastic features being contributed upstream.
This will require, maybe, like, I said, more manual configuration from the user, a little bit less user friendly. The feature will be until we add this automatic detection.
Did I explain it clearly? Or maybe you guys have any questions? Please go ahead.
**Shawn Maddock** 32:15 Yeah, that all makes sense. I think I was the one last week that asked about documentation. I had just seen a Pr. Into the operator repo for Php. And I was wondering if on the opentelemetryio site under the Php. Section, if we should be mentioning, hey? This operator exists for Php.
But.
**Sergey** 32:39 Doesn't exist right? So.
**Shawn Maddock** 32:40 Ready, yet so.
**Sergey** 32:41 Yeah, yeah, not ready yet, for sure. Yeah, I completely agree with you that shortly after contributing like having it done, we also need to update the documentation. Yeah. But it's probably gonna be the last one of the last steps.
So there is some work to be done there. Yeah, definitely doesn't exist. Far from it.
**Shawn Maddock** 32:59 Sounds, cool.
**Chris Lightfoot-Wild** 33:05 Now that.
**Sergey** 33:06 We had again. I don't know is Sean, are you? Are you? Do you know, like there are people that want it like?
Because the truth, we had similar functionality for classic Apm. Agents before open telemetry. Big boy, elastic, started, switched completely to open telemetry we had. I don't know if you're familiar. We had our own Pm. Agents in elastic. So other agents already implemented this functionality and some of them were used.
Java, I think, mostly, you know. Js, but nobody requested us to implement it for Php, so we're kind of like on the impression that so far we didn't see the users really wanted it. But maybe the completely different group users came for open telemetry. So, Sean, this is something that you would like to use this Kubernetes operator.
**Shawn Maddock** 33:54 No, it wouldn't apply to our environment other than the the one person that asked in slack, and I think you responded to him a couple of weeks ago.
I haven't heard any requests for it. I think Cedric is the person you were thinking of earlier that had contributed a bunch a couple months ago.
**Sergey** 34:11 Possibly he joined, maybe a couple of months ago he contributed a bunch, and he mentioned that maybe he would want to find a way to to make deployment in Kubernetes environment easier. So that's exactly the point of this operator.
Yeah.
**Shawn Maddock** 34:25 What we're not using kubernetes currently. So it it would not apply to us.
**Sergey** 34:31 Yeah. So it's just a really kind of like interesting combination of a user that they would be interested in this because it must be devops, I guess, because they don't want even to change the container. So yeah. So because with elastic, you can deploy open telemetry even without changing the application, but you will need to install it in in the container. So this takes it a little bit, even one step further, like I said.
So, how many users really want this ease of deployment for this particular use case?
that's interesting question.
By the way, I wonder if do you guys like consider, I don't know. Like, do you know, if other groups collect any kind of telemetry like, what kind of people use open to Php like. It would be interesting to see, like how many people even use it in the context of Kubernetes.
But I wonder like if we we do plan to collect this information as part of the elastic given it to to its cloud. But I I wonder, like how open open source teams approach this telemetry question, because sometimes it's interesting, right? When you decide which features to even consider implementing. If nobody uses open for Php in Kubernetes context.
Well, I guess it's a bit chicken and egg right? Maybe they don't use it because it's harder to deploy if it will be easy to deploy, maybe they will use it. But besides that, have you considered like, do you think it's important to consider gathering some kind of telemetry, understanding how pro how the speech opportunity from Php is used.
**brett** 36:12 Yeah, it would be really nice to know. Perhaps even more generally.
where is Php used? Might might help so I know that Zend, or perforce sort of does a like a survey every year of developers because they email me. For you know, the state of Php, which might might give at least give an indication of how many people are running Php. In general on Kubernetes.
and I know at my job we do. But I don't think I mean I'd be interested in trying out the operator. But I just build open telemetry into into our images. So that from the get go.
**Sergey** 37:00 Yeah, that that's what I meant. Like, it would be interesting. Yeah. So we gather like a like a special job agent. They have a multiple ways to deploy the agent. So they gather the statistics and to understand how people deploy it.
okay, I mean, we'll definitely share data that we collect for elastic. So those can. But I was just wondering if it's something that because essentially we do it with our ui. So I guess for peach being kind of like a back end product, it might be much harder to together telemetry for it right? Because most likely will run in some kind of Dmz to not be able to send, even if yours agree to allow it to send.
But I don't matter. I was just wondering if if it's something that you felt, but I guess we'll see how it goes if we have any hard questions that need to be answered.
But 11, 3, maybe we will reevaluate them.
**Shawn Maddock** 37:55 Does the Cncf. Have any policies on there?
Incubating and sandbox projects as far as privacy policy for users? Or is it up to each project to define that.
**Bob Strecansky** 38:12 Oh, no, it's a good question.
I'm sure they they have the. They have lots of different policies like that, and they're all strewn all over the place. I'm sure you could ask in I'm sure one of the Cncf. Slack rooms would have the answer to that. I just don't know which one.
**Sergey** 38:31 Yeah, privacy is one aspect. But you also need to have infrastructure to collect it. Right? So essentially, you need to keep something going going in the cloud that the stuff will be able to to be sent home.
So it's just interesting how if there are open source projects, products?
Cnf, right if they already have. Maybe some Cncf. If they have already, maybe something implemented that other projects can integrate with interesting question.
Maybe I will do some search.
**Bob Strecansky** 39:02 Oh!
**Sergey** 39:04 Yeah, so so that's about it. So if you guys like, like, I said, if you want to find out to see if you can. If you want to contribute or see how to move it forward, please let me know.
And obviously.
after we we're done with this, so like, I said. Our plan is finished contributing elastic stuff upstream and then on base of it. We'll finish the work on. If by that, by then it's not the ones. Further, we will go back to the operator and finish it.
So we didn't abandon it. We plan to finish, but now we just reduce priority for it a little bit.
**brett** 39:41 Yeah, I like that plan. Personally, I'm I'm I'm more excited about the sort of the the benefits to the you know Api and our SDK of of some of your contributions, and I am of the operator.
But that's just my personal opinion.
**Shawn Maddock** 39:57 Same.
**Sergey** 39:58 Yeah, we were mostly motivated just because of alignment with other languages. But then we discussed it with our Pm. And explained it it. This. It was not issue in for classic elastic Ipm agent. So that's why it got degraded in priority. Yeah.
downgraded.
But I will keep you posted.
**Bob Strecansky** 40:20 Thanks. Thank you, Sergey.
**Sergey** 40:22 No, you're welcome.
**Bob Strecansky** 40:25 Any other topics before we adjourn today.
Thanks. Y'all see y'all on the Internet.
**Chris Lightfoot-Wild** 40:35 Hello! Hello!
**Bob Strecansky** 40:36 Oh, before I forget I am out of, I am out of the office next week for 4th of July.
I will be far away from a computer. We'll catch you all the next week.
**brett** 40:46 Bye, bye.
**Chris Lightfoot-Wild** 40:48 Yeah.
