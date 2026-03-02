SIG: PHP SIG
Date: 2025-07-09
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/bqG8MOiS9vrtQjDyDwISsd3xQrVLe7i69yUL2NqKP9a3JO4sttwPVXKFKGmdAqUl.O4vUGl1K-PNo3G4z
============================================================

## Zoom Recording Transcript

Bob Strecansky 00:01:12 Hey! Chris.
Chris Lightfoot-Wild 00:01:18 Yeah. Well, okay.
Bob Strecansky 00:01:21 Doing good. How about you?
Chris Lightfoot-Wild 00:01:23 I am all right. I'm curious
welcome back, I guess, of the week off. Did you have a good time.
Bob Strecansky 00:01:29 Yeah, I want to. I'm sorry. I'm just finishing brewing my coffee, but you can watch me do that.
I did. I went to went to Boone, North Carolina. My dad bought a new house there, and it was really nice to have some family time.
Chris Lightfoot-Wild 00:01:43 Oh, nice!
Bob Strecansky 00:01:45 It's it's about 5 and a half hours. North of where I live.
Chris Lightfoot-Wild 00:01:51 Oh, cool!
Bob Strecansky 00:01:52 So the temperature was like
trying to think euro style. The temperature was like almost 8°C, cooler there than it was at home. So that was that was a nice reprieve
it has been. So. It's been like
consistently 34, 35 here every day.
and it's like it's like 35 degrees at 9 o'clock at night, too. It's like you'd get no reprieve from it at all.
Chris Lightfoot-Wild 00:02:28 Well, the room I'm sitting now says it's 28 degrees, apparently.
Bob Strecansky 00:02:32 Is that that's pretty hot for you.
Oh, it's horrible. Yeah, we don't have air conditioning. So oh, yeah, that was
Chris Lightfoot-Wild 00:02:41 Open the window, and hope it cools down is the fact.
Bob Strecansky 00:02:45 I feel like I feel like the goofy American. But air conditioning has been baked into our DNA and is absolutely vital here.
Chris Lightfoot-Wild 00:02:52 Hmm.
Bob Strecansky 00:02:54 The I had my air conditioning unit died this week, and it turns out it was so hot that one of the lead, like we. I think we had a power surge, and one the lead wire from the house, the air conditioning and just just integrated, melted.
Chris Lightfoot-Wild 00:03:12 Hopefully. Sorry. Now you're comfortable.
Bob Strecansky 00:03:14 Yeah. Oh, I got. I got very lucky to get it sorted quickly.
See?
Alright! We'll wait a couple more minutes for people.
Chris Lightfoot-Wild 00:03:26 Hey? Bo as well. Paul.
Pawel Filipczak 00:03:28 Hey, guys.
Chris Lightfoot-Wild 00:03:30 What's it like? Where you are? It's in Poland. It's quite hot.
Pawel Filipczak 00:03:34 It's 19.
Chris Lightfoot-Wild 00:03:36 19.
Bob Strecansky 00:03:36 Oh, perfect!
That's why you were smiling while we were talking about it being super hot.
Pawel Filipczak 00:03:41 It's dog and rainy. So oh, it's okay.
Chris Lightfoot-Wild 00:03:45 To be fair. It is actually 17. Outside the room is just a bit of a heat trap, because we've got the skylights so.
Bob Strecansky 00:03:52 Oh!
Chris Lightfoot-Wild 00:03:53 And I kind of like almost a bit frugal. So oh, you know, I paid to heat the house at times of the year. So when the free heat comes in, I'm like, let's keep it just supper.
Bob Strecansky 00:04:04 Lots of people. Lots of people pay to go this Sauna right?
Chris Lightfoot-Wild 00:04:07 Oh, so sorry!
Bob Strecansky 00:04:08 I said, lots of people pay to go to the Sauna.
Chris Lightfoot-Wild 00:04:10 Yeah, absolutely.
Bob Strecansky 00:04:12 Got it right in your home.
Sergey 00:04:16 Hi guys.
Bob Strecansky 00:04:18 How are you?
Sergey 00:04:21 I don't know.
Well, we'll celebrating 1st of July last week.
Bob Strecansky 00:04:29 Yeah, we went. I went to my dad has a house in Boone, North Carolina, which is like 5 h north of where I live, and
good reprieve from the heat.
It's in the mountains.
Sergey 00:04:41 Is Myrtle Beach? Is it North Carolina, or.
Bob Strecansky 00:04:44 They? They are both of those places are in North Carolina, but they're probably about as or sorry. Myrtle Beach is in South Carolina, but those are about as those are about as far away as you can get in the Carolinas from one another.
Sergey 00:04:56 So you're very far from the ocean. Then.
Bob Strecansky 00:04:59 Yeah. Yeah. Oh, yeah. Booty.
Sergey 00:05:00 He'll do it.
Bob Strecansky 00:05:00 In the Boone is in the mountains. Yeah. And
I, it's it's funny that you mentioned Myrtle Beach, because that's like
that's like 2 gangs fighting each other. I I moved to Hilton Head Island, South Carolina, when I was in high school, and, like those are the 2 competing tourist towns in South Carolina, so like
we don't like the people from Myrtle Beach. It's like kind of the joke.
It's not true. I like people from Myrtle beach, but
stupid American stuff, all right. Well, we can get rolling, and if other people show up, other people show up.
Looks like Brett has 2 agenda items for today. So I'm assuming that he will show up.
Sergey 00:05:44 We don't expect bread. Here's Brett.
Bob Strecansky 00:05:47 Speak of the devil.
Hello, Brett!
Can you hear us?
We can't hear you, I think.
Year of the Linux desktop.
Brett McBride 00:06:11 Can you hear me now?
Bob Strecansky 00:06:13 Yes, we can.
Brett McBride 00:06:15 That was easy.
Sorry I'm late.
Bob Strecansky 00:06:18 You're not.
How are you?
Brett McBride 00:06:22 Yeah, I'm good. Thank you.
Bob Strecansky 00:06:26 It's good.
Maybe it's not keeping you up too much. I hope.
Brett McBride 00:06:30 Not too much, no.
Bob Strecansky 00:06:32 That's good.
Alright! Let's let's get rocking here, Brett, I saw you have 2 agenda items today. Would you like to talk about this 1st one.
Brett McBride 00:06:40 Yes, yes. So this is about semantic conventions. That so I've I've
I think I got into trouble trying to build
1.33, I think. Like, there's just been a there's been a lot of changes with with how they generated
and there were some duplicates anyway. So I I went back and
decided to go and look at what Java is doing, because, although we originally copied Java 5 years ago. They've evolved, and the way that everyone sort of generates semantic conventions has has evolved since then. So this is a
Hopefully, again, spec compliant way to do it. It's certainly the way that it's
suggested in the spec to do it, and I
fairly closely copied Java's implementation, except that our
what do we call it? Incubating? Section is just in the same repository. I haven't. I haven't gone to the trouble to sort of split that out and and do it separately. So
so what we have now, if you were to look at the the file diff is basically one file per
type of or category of of semantic conventions.
and then obviously a lot more in incubating. And the way it works is stable is everything that's marked stable in the simcom sort of registry and incubating is everything that's stable and everything that's experimental. And it's worth noting that deprecated things are not
not included, which is what Java does.
Chris Lightfoot-Wild 00:08:40 What was that? So? Is it incubating? Is stable, and something else.
Brett McBride 00:08:44 Stable and experimental or development. Yeah.
Chris Lightfoot-Wild 00:08:49 So that the All, all the stable attributes are still in incubating, as well.
Brett McBride 00:08:54 Yes, yes, and and look, I assume I thought about that. And because I originally didn't do it that way.
And then I thought, well, that's actually going to break things. If you don't do that, because when things go stable they're going to disappear from incubating, and then anyone who's relying on that
is going to have broken broken code, which is not what you want when something goes.
Chris Lightfoot-Wild 00:09:18 Is it a good while to maybe extend the stable interface with incubating, and then
you can just move it from incubated upwards. If you needed.
Brett McBride 00:09:29 I think I think I think the expectation is.
you would notice that something has become stable and
which, from using the incubating version to the similarly named stable version.
Chris Lightfoot-Wild 00:09:47 Yeah, so do they always. They'll always stable, will always be part of incubating as well, though.
Brett McBride 00:09:52 Yeah, yes, it would be.
Chris Lightfoot-Wild 00:09:55 Okay.
Bob Strecansky 00:09:56 That's 1 way you can frame it the other way you could frame it is that everything is always incubated. Nothing's perfect.
I'm I'm saying, I'm not saying that that's how you. That's what it means. It's just a silly way for me to remember that stable and computing are the same thing.
Chris Lightfoot-Wild 00:10:09 Yeah, very difficult, either. But I'm just curious.
Brett McBride 00:10:14 Brilliant.
Sergey 00:10:14 3 of or 2 groups just to clarify are those
stable, stable, and incubation, stable incubation.
not stable? Or are there only 2 groups in Cuba and stable, and in Cuba, not stable. How? How many groups are there.
Brett McBride 00:10:30 There are 2.
So hang on if we if we go back to what's in semantic conventions,
somatic conventions are either stable development or deprecated.
So we're we're ignoring, deprecated and stable is stable. Incubating is stable and development.
Sergey 00:10:58 So stable is reused. The term stable is just reused, one is on top level, stable stable, and one is inside the incubation. There is also stable. Subgroup of incubation is that.
Brett McBride 00:11:10 No.
Sergey 00:11:10 I have a twice mentioned stable.
Brett McBride 00:11:13 No so stable stable isn't actually mentioned in incubating. It's just the contents of the incubating
interface.
Well, this is yeah, the the codes that are in there are everything that's marked stable and everything that's marked
development.
Are there some other space.
Shawn Maddock 00:11:41 Differences between incubating and stable.
Brett McBride 00:11:44 Sorry, Alina. Yes, there are.
There is a name. The and the only difference is the word incubating in the namespace.
Shawn Maddock 00:11:51 Okay. So if you use incubating in the namespace, then you can use all of the attributes you too.
incubating out, then you only have access to the stable attributes.
Brett McBride 00:12:01 That's right.
Yes, I'm still calling him unstable. That's that's the 1st
thing I need to fix in that code review.
Sergey 00:12:16 So, instead of unstable, you actually meant to incubate it.
Brett McBride 00:12:18 I did. Yes, I I originally did it as unstable, and had.
and and unstable only included development
in it. But then, when I looked at
more closely at at Java's implementation. I I saw the sense of of why you would.
Why, you would do that.
Sergey 00:12:42 Could be.
Brett McBride 00:12:42 Because otherwise incubating is very unstable because stable things disappear from it, and code breaks, which is probably undesirable.
Sergey 00:12:52 So incubation is almost the same synonym to experimental. This is what we call experiment you called experimental sum of the flags. So this is the same meaning. Kind of incubating experimental.
Brett McBride 00:13:02 I think so.
Sergey 00:13:04 Okay makes sense. But just to make understand. So the goal is to essentially say that that
incubating will also include stable stable like a top level stable.
Brett McBride 00:13:14 Yeah, it does.
Sergey 00:13:17 And it's just to allow people to reference something kind of like. I'm just trying to understand, what is the the use cases to essentially allow people to reference something that was an incubation, but then was moved to stable. And then they don't need to notice that it automatically continue working for them.
Brett McBride 00:13:34 It will continue working. Yeah. And then, like, it's up to them to notice that the, you know, like the the incubating
semantic convention I was using has now become stable and is available in this repo. So I should change that namespace
but we won't, but it won't disappear on them.
Sergey 00:13:55 Hmm!
But
I wonder, wouldn't it be like you? Don't foresee that there might be people kind of like using all the attributes from unstable from incubating, even though they already unstable. They just didn't know. I guess
if they look at the code they should see it like the concern is that something will be well, I guess it will become stale like that right? It will stay there still. Reference incubating and kind of like. If you want to understand. If the whole piece of code relies on something that is not stable, it will look like as if it does, even though it doesn't right anymore.
I wonder if it's if it's gonna be an issue?
I guess you can solve it like, if you can do some more deep analysis.
Brett McBride 00:14:42 Yeah. And we were sort of talking about this last week. I think you know, we we could have a
a check for things that are relying on, on unstable
or incubating, just just as a warning
but I think personally, I think I would rather people kept using incubating things references for too long than complain to us because the SIM conf I was referencing in incubating disappeared because it's stable.
Chris Lightfoot-Wild 00:15:16 Right.
Brett McBride 00:15:16 Yeah, I I guess I wouldn't expect something going stable to cause
code to break. And I think that's that's the that's what would happen if they disappeared from incubating.
Sergey 00:15:29 Right. I definitely agree with you that this sounds like a simplest solution. I think. Let's say it's kind of like benign change, right? Moving something from directly like, not even changing its meaning or its syntax right? Moving it directly from unstable to stable. Sounds like benign change, and we don't want things to be kind of like requiring manual intervention just to accommodate the change.
But I wonder like if it better will be served by some kind of like migration that you can apply to your source code.
and it will do it instead of kind of like keeping this stale reference and looking as if you're still depending on something unstable.
But I guess it will require to implement that migration thing.
Brett McBride 00:16:09 Yeah. And and then also, these aren't just used by our code
in our SDK, and in our country repo. You know that people do. Manual instrumentation like these could be used absolutely anywhere in in a bazillion code bases. So.
Sergey 00:16:24 Yeah. But by migration, I meant like, I don't know. I heard about like language like Russ. They supposed to address this kind of like breaking changes that can be automatically fixed in the code, some with some kind of like migration thing, but I don't know. I never saw it in in action. So and definitely, it sounds like it will require additional. But so I just wondered. Maybe it's not even an issue. I'm just noticed that it will keep this stale references if it's something stable. But maybe you're right like in our code. Maybe we can address it by just search and replace
that can be done on demand kind of like if it will become something that is important. But I agree, probably keeping code not not breaking. The code is probably more important. Yeah.
Brett McBride 00:17:03 Yeah. And I mean, in theory, we should be able to generate at least at least, and and maybe an issue or something, for
you know, we've or even in release notes. You know, we've generated a new version of
semantic conventions, and the following things were stabilized
in this release, and the following things were deprecated, and you know, you know, we give people more information about
about what's changed. But but I think it will be up to developers to
update their code from using, you know, incubating to to stable things when things do stabilize.
Chris Lightfoot-Wild 00:17:47 What what happens if someone's using something that's incubating, and then it never makes it stable and gets deprecated. Would we drop it.
Brett McBride 00:17:54 Yeah, it would be dropped. Yeah.
Chris Lightfoot-Wild 00:17:56 Because then, if you have a package with a dependency
like just on a minimum version.
and then someone you know the
app developer just updated the dependencies.
Could that breaks breaking stable or.
Bob Strecansky 00:18:12 I know. I know the semantic conventions working group is like being unbelievably diligent about trying to not deprecate stuff. You know. They're trying to follow the model of like. Be very, very conscientious about what goes into semantic conventions, and if you, if you're going to deprecate it, has to be for a damn good reason, and like I don't think that's the case we should be optimizing, for often it is a foot gun, for sure.
but I don't. I think that that's not. That's not the intent of the semantic conventions working group. I think they're just trying to
you. They're trying to use the incubating playground to like really, really battle, test things before they go to stable.
Brett McBride 00:18:52 Hmm, but but we and everybody should be careful about using not yet stable
semantic conventions, because they might disappear. And that's that's sort of the.
Chris Lightfoot-Wild 00:19:08 Yeah.
Brett McBride 00:19:08 That's that's that's the risk.
Chris Lightfoot-Wild 00:19:12 So, if bucket.
Shawn Maddock 00:19:13 It might.
Chris Lightfoot-Wild 00:19:14 Really careful about using them. In the 1st place, social.
Shawn Maddock 00:19:19 I was. Gonna say, it might also just be a case of
in the composer. Dependency is like binding to it
a specific dot version instead of but I mean.
I guess if we're not including the deprecated attributes, then it's no longer semantically versioned, because
if an attribute gets deprecated, it is a breaking change in our implementation, because it's disappearing.
Brett McBride 00:19:51 It is, and we sort of give ourselves wiggle room there because they're all marked as experimental, and and I guess the point of it being in incubating is like you shouldn't rely on this.
and and perhaps we shouldn't be putting them into. You know our country modules until they are stable, which is, when we can have a much higher degree of confidence that that they will
be here for a long time.
Sergey 00:20:23 Just to clarify man and make sure I have a correct understanding. So we only have 2 groups, right? The stable, which is regular namespace, no markings. There.
Brett McBride 00:20:30 And rude.
Sergey 00:20:31 Incubation. Just 2 groups. That's it. Right.
Brett McBride 00:20:34 Correct.
Sergey 00:20:34 Okay. Thank you.
Brett McBride 00:20:36 Branch.
Yeah. So I've noted, anyway, in the in the Pr. I've noted a couple of of questions for for discussion. I think we've covered them here, anyway. But
yes.
So this is a. This is a fairly big change, but I think it's a
it's a good one moving forward.
Sergey 00:20:57 I also noticed you included the incubation in the name of the interface as well. Not just namespace. Or
is that just to make sure the.
Brett McBride 00:21:08 Yes, I did. I copy Java.
Sergey 00:21:12 This is what they're doing, Joe. Okay? So it's kind of like, drive the point home.
Brett McBride 00:21:16 Yes, a couple of.
Sergey 00:21:17 Far.
Danger. Okay.
Brett McBride 00:21:20 Yeah.
Yeah. Sounds good.
Yes.
Bob Strecansky 00:21:30 John noticed our build. Php, based. Job has been failing for a while, is taking greater than 5 h 12 months ago, and then consistently greater than 6 h of the github. Max.
Brett McBride 00:21:39 Yeah. So I had a bit of a look at this today.
I think github runners are just slower than they used to be.
So I did actually massively improve the performance of
the my local build. And it's Grpc, it's all Grpc, it's basically.
Bob Strecansky 00:21:57 Yeah, I would bet.
Brett McBride 00:21:58 Consequence that we do in that image.
So I got it down from 40 min to about 13 locally, simply by switching to Debian. Apparently it's just a lot faster to build Grpc with G. Lipsy than muscle.
But that had no practical effect in the like. It's still timed out after 6 h. So I think we're just starved of of CPU resources in in in the public Github runners.
Bob Strecansky 00:22:30 You know that.
Sergey 00:22:31 Is there maybe a possibility to cache the image with your PC. Already built.
Brett McBride 00:22:39 We have to build it. That's the thing it's got to come from somewhere, and I'm not aware of any
Sergey 00:22:47 Is it? Jrpc. Php. Extension.
Brett McBride 00:22:50 Yes.
Sergey 00:22:52 Okay. So if we pre build it and then upload the image to docker hub and then use it in
in the in the runners.
Brett McBride 00:23:00 Yeah, that could do it. Yeah.
Bob Strecansky 00:23:02 I think.
Brett McBride 00:23:03 The only someone builds it manually and.
Sergey 00:23:08 Well, it's better, probably, to to put this build script in the repo, but just you run it only when you need to update the Ver. Like whatever depends.
like a version of your PC. Or whatever. When you update it, then you will upload the image and.
Bob Strecansky 00:23:23 But then that puts the onus on us to watch and build and make sure.
Sergey 00:23:28 No, you don't need to. But here, what is the dependencies like pinned to a particular version of your PC. Or just latest like, what is the.
Brett McBride 00:23:35 Latest.
Bob Strecansky 00:23:36 Yeah. So I. So I have opinions on this. I know that there are private Github runners that other Sigs are using. We should probably find out a little bit more about how, if we can use those, too, because I'm sure the public ones are just
getting slammed more and more, you know, and
but I also think that that might be bandaid on a bull hole right like we might want to figure out how to get this build happening a little bit faster, maybe. What Sergey said, maybe with some other Github optimizations whatever.
But I think
we I think it's definitely thank you for calling that out. Shawn is probably something we should spend some time trying to figure out how we can make that a little better.
Brett McBride 00:24:15 Hmm, and and just to give some history, the main reason for for even doing having this image, in the 1st place, was to
pre-build Grpc into into a Php image for developers, because 45 min is a really, really long time to to wait for a docker. Build.
so that that's
that's the only reason. Otherwise, you know, you can just build this locally. And in fact, it's
with some changes I made today bearably slow to to just build locally.
But yeah, that Grpc is responsible for 90 something percent of of this entire build time. So so unless we can get. You know.
somebody other than us
building the Php Grpc extension. That we can pull into to the images that we want.
I'm gonna maybe we just drop this image.
although if there are private runners, that's great. But I thought that the equinox bare metal ones we had certainly went away fairly recently. They were. They were cool. I never really got to use them much, but
I wasn't aware of there being a replacement.
Bob Strecansky 00:25:43 Yeah, I I don't know all the details. I just kind of just remember that in passing from one of the Maintainers meetings, so.
Brett McBride 00:25:48 Hmm, okay.
Bob Strecansky 00:25:49 There's got to be a place where that's built already, though right like this is, we're not the 1st people to build. Php, Grpc.
Shawn Maddock 00:25:57 Sir, he doesn't have it, does he?
Brett McBride 00:26:02 Sorry, who sean.
Shawn Maddock 00:26:03 3. The Php apt repo Maintainer.
Brett McBride 00:26:13 I don't know.
I'm not sure that I know which which one you're talking about.
Shawn Maddock 00:26:23 yeah, it's nice. So Php, doesn't have an apt repo themselves, and there's a
a contributor. He just goes by Surrey, SURY, that every time Php releases a new version
builds Php for Debian based Linux and hosts.
Repo. So if he has it, I mean.
Bob Strecansky 00:26:54 Oh, man!
Shawn Maddock 00:26:55 It's as official as you can get for.
Brett McBride 00:26:58 Can.
Yeah, okay. I mean, there's probably also a A Deb package. It's just that we're not using.
We're not using a packaged version of Php, we could switch. I I just want something that works. I don't.
Pawel Filipczak 00:27:13 Problem with that with the repo, because if the Php. Is going to be deprecated, they are canceling the bills, and the packages are not available from.
I I think, quite, quite, you know, quite soon after after the deprecation of the Php. So
that might be an issue.
Sergey 00:27:35 But deprecation, you mean end of life like, for like 8 0, they removing the packages for that for php, 0.
Bob Strecansky 00:27:42 Why don't we? Why don't we create a Github issue for this? And we can discuss it there and come up with a good plan for making this a little better.
Brett McBride 00:27:49 Hmm, yeah. Good idea.
Bob Strecansky 00:27:55 I can. I can do that, or if somebody else wants to make that.
Sergey 00:27:59 Sorry, Bob, can you repeat that? What? What was the suggestion.
Bob Strecansky 00:28:03 I'm going to make a Github issue so that we can discuss this and come up with a strategy, for
it's.
Sergey 00:28:09 Thank you.
Bob Strecansky 00:28:20 Okay, I'll fill that out later.
Brett McBride 00:28:22 Yep.
Bob Strecansky 00:28:26 Interesting.
Shawn Maddock 00:28:27 We have time. I had one question.
Bob Strecansky 00:28:30 Shoot.
Shawn Maddock 00:28:32 I know we have. The clock component in Api.
Is running into an issue
yesterday. With the react developers that the sorry this is
tangent on a tangent. The Psr transport uses sleep time, Nano, and it's the only
sleep function we use anywhere in our
You're still sharing your screen. By the way, I don't know if you care.
Bob Strecansky 00:29:07 Oh, sorry!
Shawn Maddock 00:29:13 Anyway, it's the only place that we use sleep, and it's blocking. So I was wondering if
we could add some sort of sleep or pause or delay function to our clock component
and use that and that way.
like for react, we could just make a pluggable clock interface
instance, that uses react instead of the system sleep.
So I didn't know if that was feasible, or I just wanted to get people's opinion before I.
They did an issue or a Pr. On it.
Brett McBride 00:29:52 Yeah, yeah, it's feasible. I mean
proof that it can be done. I wonder whether spi service provider could could be used to
implement a
like a, what are we calling it? A sleep implementation or something? Just because that sort of has package dependency
stuff built into it?
Yeah. So you basically, you're wanting to swap out.
you know, at a blocking sleep function for a different sleep function. Conditionally.
Shawn Maddock 00:30:28 Alright correct. And since we already had the clock component, I was thinking
like there's already a set default
public function for that. So if we just added a sleep function to the clock interface
is, is that a.
Brett McBride 00:30:45 Hmm.
Shawn Maddock 00:30:45 An appropriate solution to the problem or.
Brett McBride 00:30:49 Yeah. And that's why I mentioned spi, because,
yes, being able to inject a sleep function would be would be cool. But also we'd probably prefer
developers to not have to manually do this.
You'd sort of want it to, either, to choose the correct one
and maybe it doesn't have to be spi, but but you know some sort of check with the, you know, the default. Sleep implementation changes based on whether it can find, react or not. For example.
Shawn Maddock 00:31:27 Sure.
Bob Strecansky 00:31:29 Yeah, I would be. I would be
I'd be hesitant to change the clock like our clock function unless it was like, unless it was necessary, because it's 1 of like the oldest, most used, like one of the most important parts of the Api. But
I could. I could see how this could be useful. But I agree with Brett. I'd like to read and investigate spi interface first, st but then, if we have to do something with the clock, that's fine.
Shawn Maddock 00:31:54 Sure I I have not looked at Spi at all. I know there's been discussion on it. But I've just never
poked around with Tobias's repo.
Sergey 00:32:04 Sure. May I ask a question? So this sleep, in which context would you like to call it? Is it in the context of one of the instrumentations or.
Shawn Maddock 00:32:12 It's it's used in the Psr transport.
Currently.
Sergey 00:32:18 Psr. Transport itself or instrumentation for Psr. Transport.
Shawn Maddock 00:32:21 Psr. Transport itself.
Brett McBride 00:32:23 Be part of the retry.
Sergey 00:32:26 Then why would it depend on the clock that was injected into the open telemetry?
Maybe I'm missing something.
It's not currently I was.
Shawn Maddock 00:32:37 Would like it to be, was trying to
figure out a way to make it pluggable. So it wasn't hard coded to use the internal function.
Brett McBride 00:32:49 May maybe, Sean, just go back and describe the problem again. So
so in Psr transport, there's there's a sleep, and that's blocking. And that's a problem for react.
Why?
Shawn Maddock 00:33:03 It. It just slows down the
I guess it's not technically asynchronous, but the
Brett McBride 00:33:13 Loop.
Shawn Maddock 00:33:13 Concurrent. Yeah, the the loop it it stops
when you say react, you mean react. Php, library.
Yes.
Sergey 00:33:24 Okay? So it's it's nothing to do with the open telemetry like instrument and stuff. It's just pure library itself. React. HP, plus Psr transport for it.
Shawn Maddock 00:33:35 Sorry.
Sergey 00:33:35 Solution be, wouldn't the solution be to implement if you want to inject the same clock
that you want to somehow mock the real time, including the sleep.
Wouldn't the solution be then, to create this clock and implement both interfaces from opentelemetry? If you want to inject it to opentelemetry? And then also, whatever interfaces you want to introduce in that Pcr use case
that will also mop the sleep.
because otherwise I'm not sure, like, if open telemetry itself doesn't never call this new method that you would like to add to clock. Then what is the point of having it for the to the interface that has been injected into open telemetry.
Brett McBride 00:34:13 And that's why I was asking.
Shawn Maddock 00:34:14 Group.
Brett McBride 00:34:15 Yeah, I think I understand what Sean's getting at is that instead of having a hard coded sleep for a period of time in our Psr. Transport, which will be part of
like if the 1st request fails, wait a period of time, and then send the next the next retry.
instead of that being blocking, we should defer to
a an interface or a method on on the clock.
Sergey 00:34:43 So it's a Psr transport that used in the context of open telemetry. It's not just something outside open telemetry. Okay.
Brett McBride 00:34:49 Yeah. Yep.
Shawn Maddock 00:34:52 Thank you for explaining that Brett.
Sergey 00:34:57 And the the use cases of try to kind of like mop the clock and, like completely control, create artificial clock for testing.
Shawn Maddock 00:35:04 The clock was just
the 1st idea I had of how to solve the problem. I'm not tied to that.
The the actual problem is swapping out the sleep
function. So if we do that with psi.
or if it's not doable at all like all of these are
like we could just write our own transport and use that instead. That's also an option.
Brett McBride 00:35:34 Yeah. So we so we want to somehow abstract away this sleeping mechanism so that it can be non-blocking
for for some runtimes.
Sergey 00:35:47 It can be unlocking, but it must be consistent with the other functions of the clock. Right? Like.
It should make sense in the context of what is required
like, if it waits, I mean, I I guess I sleep doesn't guarantee that it will sleep all that time right?
Maybe it says at all.
sleep at the most. I don't know what are the guarantees of the sleep call.
I think it can exit the La right.
but I'm just trying to understand what is the use case. So let's say, you will implement that sleep as just exiting immediately, not sleeping, or
what's gonna be the implementation that sleep that will satisfy it not being blocking, so it will not sleep.
Brett McBride 00:36:30 React. It just means that react can do other work while that sleep is happening.
Sergey 00:36:37 Right so. But you. But you need to somehow suspend that threat of execution
and not allow it to proceed, because, in order to proceed. It needs to rely on the fact, because otherwise you will just create busy loop there and loop react. Loop will not get
not get to work anyway. Right? So if you exit directly from the sleep, then that loop will just constantly try. Be retrying. If you will try to somehow suspend inside the sleep and switch to the less other tasks that are in the backlog of the react loop event. Loop. Then how you're gonna resume that back there where the sleep was called. You need to some kind of like a fiber thing.
Yeah.
Shawn Maddock 00:37:14 And react. Already has that implemented.
Sergey 00:37:20 So so it will. So it's so you want to cover. Then fiber. Use case to spend there and allow
But I assume that sleep itself then.
So sleep on the level of
of Php itself is not fiber aware. It's not allows them to other fibers to start executing. I'm not familiar with fibers themselves, so maybe doesn't make sense.
Shawn Maddock 00:37:44 Correct. It's blocking. And I
I think I pulled an Xy problem here of introducing the solution before explaining the problem. So
apologies for that and muddying the waters. I that
I mean just to keep the meeting on time. I can create a Github issue for this, and we can
hash out the best solution there. But I mean the feedback here
has been helpful. And again, we, if it's something that's not
beneficial to the rest of the ecosystem react can just have its own
hotel transport, and we don't need to mess with hotel Corrid Hall.
Brett McBride 00:38:31 Yeah, I mean, I look, I I understand the problem. And I could see that it would be useful for well, not just react. But you know there are other asynchronous Php. Runtimes. So
so I think, yes, yes.
yeah. You just need to, I suppose, play with it and see see what works locally.
Sergey 00:38:53 But I wonder, will still be enough like just replacing the sleep. I assume the whole implementation there relies on the fact that it's completely synchronous calls right? So trying to convert that Pcr implementation to being asynchronous.
you probably would want to also all the I/O. Calls network calls to to replace them with something synchronous right.
Shawn Maddock 00:39:12 Yeah. And I mean, we've already
worked all that stuff out. We can swap. Psr, 15 and or
16 and 18. Is it 17 and 18, anyway.
that that's outside the scope of the issue.
Sergey 00:39:28 Okay.
Wonder if we discuss an ad hoc questions. Sean, you wanted to ask something else or
don't want to jump.
I wondered. I. I had a question also related to. Maybe it's the spi that was mentioned. By the way, the spi that you mentioned is it already in main, or it's something that you guys work on the on the side.
Brett McBride 00:39:51 Is it in? My? It's used in my yes, yes, we use it.
Sergey 00:39:55 So my question was essentially I was wondering, like with where
finished working on the pump, but we would like to better integrate it with. SDK, so so currently, we are setting environment variables. But instead, we were wondering if it's gonna be better to use some kind of like pluggable configuration source interface.
And I looked at the code in main, and I saw that the code that is responsible, at least for the configuration that's been passed to instrumentations. If I understand correctly that kind of like 2 ways to. There are 2 configurations. I wonder if I can share my my desktop?
If you guys, mind, let me share, just to make sure.
We refer to
So it's clear with what I'm referring to.
So I looked this this code. Can you guys see my screen?
Maybe I will make it bigger.
Brett McBride 00:40:47 Yeah, a little bit bigger.
Sergey 00:40:49 Representation mode. I think it's called, yeah.
okay, is it? Is it better.
Bob Strecansky 00:40:54 Yeah, I didn't know that existed. That's cool.
Sergey 00:40:57 Yeah, so there is this thing called. So we are inside this decay. Autoloader and I looked at the. So there is this notion of configuration that's being passed to instrumentations right?
And then there is this notion of configuration like this that can be obtained this way.
So maybe it would be interesting. If you guys, maybe can
clarify, please, what is the difference between them? It seems like this one used by Core SDK, and this one will be passed to
to instrumentations. But the way I'm looking at it like, for example, the knowledge about the file is kind of like directly hard coded here. So we're just wondering is there is a way, because I hope that the all the sources of configurations, such as environment, variables, any Ini and the file. That will be kind of like a pluggable thing that we can integrate there and add additional kind of like source, remote configuration or pump.
however, we call it, and what we discuss about layering the priority wise. So I'm wondering
how how would you approach that problem of trying to kind of like plug additional source
of configuration in the current implementation.
Brett McBride 00:42:09 Oh, God.
yep, so yes, you're right. We do have 2 different ways of of doing configuration. You've got environment variables, which is the the original.
and you know well known way to do it. And then probably over the past
year or 2 years, has been
what was originally called file based configuration. Now it's called declarative configuration. I think.
Sergey 00:42:37 And then they don't coexist. So it's either one or the other right.
Brett McBride 00:42:40 You can use either one or the other.
Yes.
Sergey 00:42:46 Because it seems to be. They are kind of like, mutually exclusive, based on this right.
Brett McBride 00:42:50 Yes, they are. Yes, so, and that's that's in the spec somewhere that and you've you've got the exact bit open. So if you've provided hotel, experimental config file, then disregard all other environment variables and go and process that file. That file can refer to itself as to environment variables. But yes, but that that's the choice where we go one way or the other for configuration.
Sergey 00:43:16 Right. But then there is also Ini right. So, for example, this uses Ini this part.
Brett McBride 00:43:22 I see.
Sergey 00:43:22 Probably doesn't.
Brett McBride 00:43:25 Yes.
Sergey 00:43:27 Why did this distinction made like? So the configuration passed to instrumentation.
The it's not possible to pass anything from in either, but for the core.
like here you. It also reads from I and I
is, that is, is, that was done on purpose or just historical reasons.
Brett McBride 00:43:45 Low configuration properties from end, despite its name, I think, probably does still look at any.
Sergey 00:43:53 You mean this one actually does read from mine.
Brett McBride 00:43:55 Yeah, I think so.
Chris Lightfoot-Wild 00:43:58 If you look at a composite resolver, I think it's called.
Brett McBride 00:44:01 Yeah, yeah, there'll be a there'll be an abstraction underneath that. But but I think it, you'll find that it it does.
Sergey 00:44:10 it's not referring to end result directly. But maybe it's somewhere behind the scenes. Okay, go, i see,
i, see so then going back to my original question, what how do you think would be the best way to try to add additional source like remote configuration? Whatever other source of configuration.
or like what you guys mentioned last time, a dot n file.
Is that something that you're planning to do? And then it will be easier to integrate or
it. It should be possible even now, with the current weight.
Maybe this is pi thing that I'm here. I need to read about it.
Brett McBride 00:44:47 Yeah? Or, yeah, we need to think about this or or is that configuration? In
what? What does OP Amp need to know? Is it just a
is it like I'm using off Amp? And here is the
host. Or here is the URL. You have to go to to get your configuration.
Sergey 00:45:10 No, I guess it's the same interface as this configuration. I mean, I I think, like this configuration that comes from this methods, I think can implement it right? So essentially just. It just provides kind of like a map interface. You give it, I guess, id, it's the name of the option, and then it will give the value right? So that you don't need to be aware of the fact that it's a pamp or anything like that.
because the Gretians already fetched the background.
and it just wants to integrate in this layers of configuration, right and just.
Brett McBride 00:45:40 And this is just to do the initial configuration, because during Runtime OP. Amp. Will change things right. But.
Sergey 00:45:47 The whole SDK doesn't support this ability of changing configuration on the fly right? We kind of assume that configuration should stay a snapshot right, because otherwise there will be inconsistencies unless you correct me if I'm wrong. Like my impression was that assumption is configuration is immutable. Kind of like. It's determined in the start, and then, at least during the request.
until we end of the request. Lifetime life cycle. It stays the same.
Or am I wrong like. I guess maybe some benign changes like log level, but even log level. If you look at the log level, I think it's it's determined at the beginning, and then just cached into static or something. So it seems to be. The feeling is that the design was which sounds fine, like I think it's even better for the user. Like, assume that, I guess, for the applications like react. Php, that might be a real issue. So maybe in that model, this thing needs to be rethought kind of like. How? What is the
what is the session? Kind of like? How we define? What is the session for which we keep the snapshot of configuration right?
But let's say, if we go back to the classical Php model when we have one request, and then the whole thing is recycled, anyway.
Then keep in configuration as a snapshot
sounds like a normal choice simplifies the whole thing right? You don't need to consider what happens if you're in the middle of work.
A configuration changed.
Brett McBride 00:47:11 That's true, although you, you and and Paul Of
know a lot more about OP-amp than than I do.
If you've already implemented it.
My! My knowledge is only pretty superficial. But I thought the idea was that it.
Sergey 00:47:28 Yeah, yeah, but we will. We will not change it after we contributed to the start of the request. I think it's like, I said, it's it's gonna be an issue for the react. Php, because it's a long running request. So we'll have to find a solution there.
Chris Lightfoot-Wild 00:47:38 Okay.
Sergey 00:47:38 But that solution is not because of a Pam. A Pam is just the 1st configuration that really makes it possible to change configuration. Right like you said after the start, but
the bigger work will need to be done in the all the places where we depend on the configuration to make sure that we provide some kind of model that allows, you know, not to be worried, that you have changes, asynchronous changes completely. The problem that those changes are asynchronous, right? So they can happen in the background.
And suddenly configuration changed on you in the middle of you, working with that configuration, and those changes can be inconsistent. Right? You read one option. Then you read the second option. They came from 2 different conceptions of configuration. They are not consistent with each other. You might be a big problem in a big problem right here.
So it's better to provide some kind of like snapshot that allows you to rely to say, Okay, this is the start of the some kind of session thing, and you know that from this point to this point you can rely on the configuration being a mutable snapshot.
Pawel Filipczak 00:48:37 And you can reread it, and you know that there will be consistency, because it's all came from one snapshot.
Sergey 00:48:43 But we'll need to define that model and to support such a cases when react, such as react when you have long running request.
Pawel Filipczak 00:48:51 So can I have something. So you're discussing it few months ago? I guess so.
The the proposal on the beginning is that we will provide a
the initial config on the beginning. So if if all pump will be fast enough to to provide a config before the request serves, then everything is okay. So we can just apply the remote config config over the
the let's say the defaults read from this other sources.
and I think that the we should introduce additional
Api for getting the dynamic config in case of the changes during the the request lifetime.
So in that case we can, of course, provide fully dynamic config with the separate interface. So if we in introduce some or update our instrumentations or SDK
in the future, then we can just get the the the fresh config, the the fully remote config
from the second interface, because in other case it will be a a nightmare to to, you know, to take to, to make a full control over the the changes during the lifetime of the request, or of the application. If it's a standalone application. So you, during implementation, you must be aware what we are doing. So if you are aware that you want the dynamic option, then we should introduce the Api for that and
pick the pick. The dynamic value, of course, the base for the dynamic value will be the defaults read from the other sources. Right? So we can mix that or create a base for the dynamic values from the rob from the request in it. Snapshot right from those. This snapshot mentioned by Sergey.
So in that case, in my opinion, it will make more sense to provide second interface
only for the implementations. Aware of the dynamic options.
Sergey 00:51:00 Yeah, we need to discuss it. Because obviously this, the interfaces currently stands. It doesn't allow for that. Because, as you saw, it's quite simple, which is okay, for now it already assumes that this is one snapshot. So this is a snapshot of the what Power says is that we essentially need to. If we want any instrumentation such as instrumentation for Reactp to be able to ask at each point, let's say it has some kind of like idle point at which it wants to reload the configuration.
or let's say it wants to somehow keep it per
fiber up, or some kind of concept of like I said session. However, it defines right inside one native Php request it will define react sessions right? Somehow. It will identify where the react request starts and ends. Then at the beginning of react request, it can call the second Api and get
updated configuration. That is most. It still will be a snapshot, and it can keep this immutable snapshot for the life cycle of that react request right? It's still relying on the fact that it's an immutable configuration, but it will be updated right? So if you want to
for long running frameworks, such as react to get new configuration, then it will be possible. But it needs to be aware, right? It needs to be aware that this is what it's doing right, that it's now acquiring new snapshot. That is the latest. And it might not be consistent with other snapshots that were taken in the past.
but you keep.
Shawn Maddock 00:52:27 You keep mentioning react like react is not
dynamically configurable. It you have to reload the process if you want to reload
configs just like any other php. App.
Sergey 00:52:39 A reason I'm asking for mentioning. React is react breaks the classical Php model of what request is right. The the Php has this lifecycle model when on each request, your memory is completely recycled. Right? An application doesn't, doesn't remember anything between the request, right? So this with this classical model. So we're currently discussing. So the the way we can allow or even react applications to be dynamic, configurable
is with this pump feature. I don't know if you're familiar, Sean. There's this new feature pump. It essentially allows us to communicate with external interface like Otlp, but complementary to it. Instead of sending to it. We are reading from it. And we are getting updated configuration. So we are doing it in the background. Currently, it's a thread. But we can do it in the background process.
and essentially at the start of each request from the from the extension, we are asking if there is a new configuration, and we build in a new snapshot and providing it to the to the SDK at the start of the request. Now, I'm talking about classical Php request in react obviously classical Php request is hijacked.
It always one request, but react. Behind the scenes runs multiple requests
that a logical request from react point of view, right
and obviously just acquiring one configuration. Snapshot at the beginning
will not provide any dynamic kind of features, because react requests can run for hours and serving actually, maybe possibly thousands of logical requests, right? And if we want each of logical requests being, you know, having access to the latest configuration or pump can support it but react instrumentation
should allow for that, like, it should be aware that it needs to keep snapshot separate for each logical request. I I hope I'm not confusing you guys. Is that something that is confusing or.
Pawel Filipczak 00:54:40 So maybe I will simplify. So it applies to each and every long running cli application which has implemented some kind of dispatcher
underneath, so it can be react, or some other rest, Api framework, or or whatever you know, providing some additional tasks. So.
Sergey 00:54:59 Mean event, loop.
Pawel Filipczak 00:55:00 Not really dispatcher. So if it if it's long running and is dispatching the task, and let's say it's it can be just long running application. If there is a need for update updating the configuration of of instrumentations during the lifetime of of this application, then we can do that now. But with the open and the separate, a Api for the dynamic values, then we'll be able to do that.
So. But we need to provide additional Api format.
Sergey 00:55:32 Anyways like putting aside the whole reaction. Sorry if it's more confusing that let's forget for the moment the whole Api. Let's assume that we want much simpler model. The the classical normal Php request tricycle model right? That we know that SDK is loaded at the beginning of request.
and then we configure it, based on environmental sources. Then SDK, just assumes that that configuration stays the same for the duration of the request. And then SDK. Doesn't care what happens at the end of the request, because the whole memory is wiped out anyway, right? So when it will be loaded for the next request, it will start a new, and everything will continue the same. And it's possibly that for next request the the configuration will be different, but doesn't care, because
there's no different. There is no way to compare what was in the previous request versus the current one
because no memory survived between those 2 requests. Right.
Brett McBride 00:56:25 Yeah. So so probably those domain questions. Then, Sergey, and I don't know if the spec talks about this. But is is
is OP-amp configuration, a complete replacement for environment or declarative.
Sergey 00:56:42 No, it's supposed to be on top of it. It's supposed to merge with the local configuration.
So you only need to provide the def like. You only say what you want to override.
It's assumed that whatever provided locally
will have low priority, so a pump will override it. But if a pump doesn't override certain options, then they will be sourced from local configuration.
Brett McBride 00:57:03 So I feel like that would be pretty easy with environment configuration, because we've already got a an ordered priority of things we look at. And we talked last week, you know, dot any 1st sorry
dot m first, st and then
environment, then dot any whatever it was. You know there's and there's 3 or 4 different things, and I think that would be pretty easy to
check.
Let's just add another loader right there on the code you you've you've got open.
How it works with declarative configuration
will be a bit more interesting.
I'm sure it's a solvable problem, but I think it'll be a lot more complicated.
Sergey 00:57:47 Yeah. So I see 2 issues like, yeah, exactly like you said. But let's say it's probably less of an issue. We can say, okay, it's not compatible. You cannot use a pump with the experimental config. Right? So essentially, pump will not work with experiment. But I think the bigger problem is that for? Let's let's say, for example, you guys plan to add support right? And I think we decided that it's going to be higher priority, that environment variables.
Brett McBride 00:58:08 Yes. So if a pump will use environment variables.
Sergey 00:58:11 Then it will be lower priority that dot. N, but this is not what we want. We want to pump to have higher priority dot n.
Brett McBride 00:58:18 Let's see.
Get higher priority. Easy. Yep.
Sergey 00:58:20 Yeah, but this way, but you can. No, but you cannot like if this will come. If this is going to be a mixed things of the actual environment variables and the pump.
you cannot unmix them from this point. So this line, essentially, currently, the way we implemented the pump is that this line returns
mixed configuration. Because we essentially, you know, when we get to pump configuration, we change environment variables. So environment variables right here after that will already be kind of like whatever environment variables at the start of the process. And on top of it we change the mind variables based on a pump. Right? So now they mixed. You cannot unmix them because they're all environment variables. From from point of view of this function it has to then assume that they are all
normal environment variables, and then it will give dot n higher priority. So in order for us to layer correctly, we do need to be able to say, Okay, we want a source that will have the highest priority. However, however, we implement that Api that allows layering the sources of configuration, we need to be able to tell. Okay, this is kind of like priority 100, while
whatever dot n had priority, 90 right? Whatever we decide, however, we decide to order priority.
Brett McBride 00:59:34 Your configuration needs to be, you know. Yes, its own object.
Sergey 00:59:38 Yes, but essentially like, I said, ideally.
Brett McBride 00:59:41 You get this variable know. Okay, now, check dot. Inv. Now, check this.
Yeah.
Sergey 00:59:46 Ideally. If we, if we had this interface like a configuration source like we, we call it right and essentially, each of the potential sources would implement this interface, and then SDK will just get these layers right within the order of priority, and it will use them. It doesn't care how they work behind the scenes. So then we will be able to inject this new source or pump, and it will just access whatever was fetched in the background by extension.
So that's essentially so. I was just wondering if you guys already planning some to do something for the 10, th then maybe we'll integrate with that, or
just wanted to understand what? What? How you guys planning to add the 10? Essentially, because if you already implement something with the 10, then it sounds like we can easily then integrate with the or pump into that
hoping that he will
not. Hard code 10. That's essentially what I wanted to make sure, because if you will hard code it like that, then it's going to be more challenging for us. But if we will implement this kind of like pluggable layer thing, then it will be easy.
Brett McBride 01:00:49 Yeah. Yeah. So so the dot envy implementation is is a pluggable layer through through Spi. Yes.
Sergey 01:00:58 Spi is already here. So it's it's it's already.
So if you, if you follow through load, config.
Brett McBride 01:01:04 Properties, from inv.
Sergey 01:01:07 So this one already kind of like relies on display.
Brett McBride 01:01:09 Yep. So see service load a load there, that's that is spi, and that is
getting all of the different things that are in component
loaders that provide the env component loader service.
Sergey 01:01:26 I see. So you you recommend me to investigate how this thing works, and find a way, how we can provide. So our class will be returned from here, and it will, but it itself currently
is not aware of these layers. Right? It just assumes that there is only one thing
so Chris mentioned this composable thing, but, if I remember composable, is also kind of like, but I will have to look at the code. But.
Chris Lightfoot-Wild 01:01:51 For this that slightly differs, that tackles some of these things. I think.
Sergey 01:01:57 But that's how we were talking about last week.
Brett McBride 01:01:59 I think that's the branch we're talking about, and that's what I'm basing. My, how we're doing.in von is is my understanding of your branch, Chris.
Chris Lightfoot-Wild 01:02:07 Oh, okay. Right? Sorry.
Brett McBride 01:02:08 Don't be uniform if I'm misrepres.
Chris Lightfoot-Wild 01:02:10 What we're looking at now, isn't that branch? Is it? So? It's slightly no, no.
you should just be able to plug it to the top with a pump, and it does result.
Sergey 01:02:18 Are you guys planning to? What are your plans for?
Try and pick that up? Because Brett tagged me the weekend? I'm sorry I've not.
Can you maybe paste the link to that which branch? I will take a look and see if I can maybe contribute something.
Chris Lightfoot-Wild 01:02:33 Yeah, I'll I'll given. It's higher priority. I'll try and get to it this week.
Brett McBride 01:02:38 Probably good good Sergey, for you to have a look at it. Then if if this is potentially very useful for you, just to have another another set of.
Sergey 01:02:45 Yeah, that's that's what I'm doing to to help you guys see if we can. Yeah, if we can build it in a way that we can easier. It will be easier to integrate such source, such as a pump.
Okay, yeah, if if you please, send somehow this link to the branch, or which.
Chris Lightfoot-Wild 01:03:00 Here, and then.
Sergey 01:03:03 Got it.
Chris Lightfoot-Wild 01:03:03 The meeting notes.
Sergey 01:03:04 Okay, I will take a look at that, and I will PIN you guys. If I have suggestions, I will add the notes there.
okay, got it. So so if I understand correctly, we can make a conclusion of this discussion. Is that currently the way it's in main, it's probably not ideal. So probably the the temporary solution will be just to set environment variables. But when we will have this handling of spi plus, then we can make it so that it will be easier to plug in. And then we'll have that new mechanism. And we can rework reliance on environment variables. Right?
Okay. Sounds good.
Thank you.
That's it for me.
Bob Strecansky 01:03:45 Alright, and we're at time good work, everyone.
Chris Lightfoot-Wild 01:03:50 Thanks very much. See you all next time.
Bob Strecansky 01:03:52 Alright!
Brett McBride 01:03:53 Great meeting. Thanks, all. Goodbye.
