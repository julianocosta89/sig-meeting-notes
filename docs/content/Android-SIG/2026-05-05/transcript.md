SIG: Android SIG
Date: 2026-05-05
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 02:44 We'll give it another minute or two and see what happens.
**Cesar Munoz** 03:00 Hello?
**Jason Plumb** 03:02 Good morning.
**Jamie Lynch** 03:05 Nope, I've got to jump in about 30 minutes, but I can make the first bit of this.
**Jason Plumb** 03:12 Cool, feel free to, like, prioritize any things about Android that you'd like to bump up in priority, so we can make sure we get to them.
And then again, the agenda's pretty light, so… Alright, well, let's get started. I put… One item in here is for us to talk about the naming of this thing, which… I understand it's clumsy, and maybe not everyone loves it.
So, it's this thing where you can suppress instrumentations by name.
So normally, it can go out and do, like, automatically detect what instrumentations are on the class path.
There are some scenarios where some of those might not be desirable, and so you can suppress them, but they're, you know, rightfully so. We're thinking about the name, it's good to think about, and… I think there were a couple of ideas, like Cesar proposed, maybe.
Disable by name… I think there was another idea from Jamie… these, like… disabled instrumentations or suppressed instrumentations. The only reason I didn't want to put instrumentations in the name is because it's already nested.
So, I mean, we could do, like, suppressed by name, I think.
is maybe… I don't know, what do y'all think?
**Jamie Lynch** 04:40 I didn't realize it was under the instrumentations block.
**Jason Plumb** 04:43 So.
**Jamie Lynch** 04:44 I'm not too fussed on my name. Like, I feel like surpassing probably does work.
In my context.
Unless folks have better ideas.
**Jason Plumb** 04:59 It is probably… probably the only, like, kind of verb form that we have in the DSL right now, so I don't know, I mean, it's… it's maybe setting a precedent that we might not want… might not want going forward, so maybe we keep it noun. I think noun is probably safer.
**Hanson** 05:19 Suppress duh?
**Jason Plumb** 05:23 We could do that as well.
Because then it goes adjective, yeah.
**Hanson** 05:30 Suppressing technically is a gerren as well, but that's… that's not…
**Jason Plumb** 05:33 Okay, okay.
studied computer languages more than I studied human languages.
**Cesar Munoz** 05:44 Yeah.
Regarding my comment, I mean… It… So, we're adding a functionality about something that is already available.
And then, that we already called enabled.
False or true.
**Jason Plumb** 06:05 So…
**Cesar Munoz** 06:08 maybe it's not a problem, but I wanted to try and convey that this is the same.
As what users do with… pre-installed instrumentations.
I, I… I mean, for us, it's clear, but I'm guessing somebody reading, you know, suppressed this instrumentation and disabled this one.
It's like, well, what's the difference?
**Jason Plumb** 06:34 So is it… is it possible to have both of those in here, then? So, like… There's another… like, you can… There's an enable, right?
I forget what that looks like.
**Hanson** 06:48 If there's an enable, there should be an analog disable, and that's okay for a verb as well.
**Jason Plumb** 06:54 Well, I don't remember if there is, but let's see. So, that class is…
**Hanson** 06:58 I mean, disable is probably more straightforward. Disabled or disable.
**Jason Plumb** 07:05 Yeah, so this is in the… Instrumentation configuration… Well, that's not right.
So this one does not have… Which one are you thinking of, Cesar?
Because this one doesn't have… these are just for the individual ones.
So within each of these, I think within each of these, there might be one to disagree.
**Cesar Munoz** 07:39 Yeah.
I think it's, it's.
**Jason Plumb** 07:43 Yeah.
**Cesar Munoz** 07:44 Base class or some… yeah, there you go.
**Jason Plumb** 07:49 Yeah, this one.
But the idea of the PR is to be able to provide a list of these that we want.
And I also added this… I also added this question, because I don't know… I don't know the answer to it, I didn't have this in mind, but if you… if these are… like, if Fragment is one of the defaults, it's one of the ones that we include out of the box.
And you put whatever the name of this fragment one is.
I'd have to go look at the instrumentation. But if you put the name of the fragment one in… In this list.
Does it work to stop it?
**Cesar Munoz** 08:33 It's true.
**Jason Plumb** 08:33 Whoa.
**Hanson** 08:34 That's true.
**Cesar Munoz** 08:35 Because the underlying mechanism, it's the same. That's why I wanted to…
**Jason Plumb** 08:41 Yeah.
**Cesar Munoz** 08:42 try to… Try to, have a, concise, or, like.
Shareable name that, you know, conveys the same, because what it does underneath is the same.
**Jason Plumb** 08:55 Yeah.
**Hanson** 09:02 I mean, isn't it the point to suppress disabled ones? I'm sorry, to disable automatic ones? Because if it's not… Enabled by default.
**Jason Plumb** 09:15 Yeah. Why would you… Yeah, there's a… there's a subtle distinction between… Included out of the box by the agent.
And found on the class path.
Those are… Kind of the same thing?
But not exactly.
**Hanson** 09:33 How many do we have that is simply Find on ClassPath, then load.
Like, how many, like, external instrumentation that's not… doesn't belong to the hotel Android package should we have? OKHTP, maybe? But, like, anything else?
**Jason Plumb** 09:50 Right, I'm thinking more about, user-supplied, or down the road, library-supplied, where you just happen to have included something that contains instrumentation, but you don't want it.
But you have all this other stuff you like.
**Hanson** 10:04 I don't know if it's within the purview of this DSL and this configuration to manipulate instrumentation that we don't know about.
**Jason Plumb** 10:14 So the idea here being, I don't know, just generically… You run… you run your app, and it picks up 10 different instrumentations, and one of them is chatty, or it's low value, and you just… so you're like, I don't… I don't need that, like, I don't care about… what these people are calling A&Rs, for example, right? My app is slow sometimes, but it's not a problem, I'm just gonna turn off A&Rs.
So you put A&R in this list, and it would be… it would be stopped.
I think that's… that's the use case, I think.
**Hanson** 10:50 And A&R being one of, the ones that the agent includes, right? And not…
**Jason Plumb** 10:55 In this example, yes.
**Hanson** 10:57 Right.
**Jason Plumb** 10:58 But it wouldn't have to be, it could also be third-party.
**Hanson** 11:01 as a controller of… so, I guess if you include a third-party library, and they have the instrumentation… they pull in instrumentation on their own.
I would assume that that third party would be responsible for disabling.
**Jason Plumb** 11:17 No, I think it's an application choice, and it could be a configuration choice, too. But, like, yeah, if you… like, imagine, a company that ships, like, 20 different mobile apps, and some of them… like, they all have common libraries, and there's instrumentation in some of those libraries, and some apps want that thing, and some don't.
**Cesar Munoz** 11:37 Yeah, the thing is that the default is that everything that's in the class pad will get automatically installed.
So… .
**Jason Plumb** 11:47 That's right, and the idea was that putting a string in here is supposed to be simpler than modifying your class path.
**Hanson** 11:55 Got it. So, we not only want to suppress default instrumentation coming from the agent, we want a general mechanism to suppress default class path picked up.
It feels like there should be an analog for the automatic class path pickup, for disabling. Is part… is that part of the file-based config?
Stuff?
**Jason Plumb** 12:23 I'm not following.
**Hanson** 12:27 So, how would you do this outside of Android? If you're using just a Java SDK, how would you disable instrumentation that automatically gets loaded by discovery or via ClassPath?
**Jason Plumb** 12:42 There are configuration flags, there's a… there's a… every single instrumentation has a name. In the Java agent ecosystem. Every instrumentation has a name, or set of names, and there's an equivalent Java system property or environment variable that you can set to false to turn it off.
So if it's, like, I don't know, vertex, if the name of the thing is vertex, it's like otel.instrumentation.vertex.enabled equals false. It's something like that.
**Hanson** 13:17 then… I feel like a similar… environmental variable pickup. Like, we can't… we can't do, you know, certain things, but we can pick up environment variables at build time. I mean, the DSL, you know, for this is also picking stuff up at build time, and then just not including in the class path, right? So it seems like… Unless we want to build an alternate path of basically… Doing this.
**Jason Plumb** 13:44 I think the ergonomics of build time environment is pretty terrible.
Like, I don't want to have to set an environment variable when I'm just compiling.
Like, you could say, you know, you could push it up to the level of Gradle and say, like, oh, there's something in your Gradle config, but I think that having… like, this was really… and this goes way back, you know, 2 years ago.
The idea was to be able to do it programmatically, like, that was first and foremost, like, the DSL is the programmatic way for application developers to control how OpenTelemetry plays with their app, and so… having… Having a way to disable stuff that's found on the class path because you include it for whatever reason, but you don't want it.
was the idea. And it was… I know I haven't looked at this in a bit, but this goes way back to some old PR.
**Hanson** 14:42 Yeah, it feels like two different sets of instrumentation, two different features rolled into one. You have one list, that looks for both instrumentation that we have, you know, within our… the agent enabling, and also ClassPath.
Like, do we want to separate that out into two lists, or do we do a match such that, you know, if it hits both, hits either, we do a disabling? I think functionality-wise, it makes sense, like, going through one place, to basically disable everything.
But then it's just… it's what you're specifying at that point. Is it the module name for what we have, or this other name that we can reference it by via SPI, it will load.
**Cesar Munoz** 15:30 It means that the instrumentations… so the mechanism, it's only one.
Which relies on SPIs. Even the ones that are provided by the agents.
By default, rely on that mechanism.
It's just that we added And… to the DSL, we added a… because we know that the agent adds this to the class path.
We added a programmatic way of Handling these instrumentations.
Without having to use their names, because they already… we know that the agent provides those. So… but the ones that we don't know that the agent provides, are left… Untouched.
by the currently DSL, and I think that's what Jason's trying to address.
The rest of instrumentations.
**Hanson** 16:26 So we provide a mapping, and the kind of internal names are the ones we use, and not the ones that are… looked for in the class path that the agent will use. And now we're saying that we also want to look for the other name that is not, you know, the Android agent provided name.
**Cesar Munoz** 16:50 Yeah, for anything that's not… built into the agent, such as…
**Jason Plumb** 16:55 Yeah, so then every instrumentation has a name, first of all, right? Like, this is… yeah.
**Hanson** 17:03 And then this maps.
Go ahead, Zelda.
**Jason Plumb** 17:07 there, yeah, there's a list of… in the agent, in our… in our build gradle, there's a list of included… default instrumentations.
with Qlik being a little contentious, I saw that comment, we can talk about that later. I didn't put it in the agenda, but there was a comment about the new Qlik instrumentation.
Right, so of this list, this is what we include by default.
So these are on the class path at runtime because we have them in our build gradle.
And then the application could choose to also include others, like OKHTTP.
Or whatever else.
Or some… you can imagine some third… Down the road, if we're hugely successful, some third-party bomb that includes, you know, a ton of instrumentations, and maybe you only want some of them.
**Hanson** 18:03 And right now, the list takes this… Short name.
**Jason Plumb** 18:09 In this PR, yes, it would be, you know, like this.
**Hanson** 18:15 But to suppress the ones that, are just on the class path, you would have to basically find, a different… name, for instance, that don't have a short name.
**Jason Plumb** 18:28 They all have a name, it's part of the API.
The instrumentation API requires them to have a name.
**Hanson** 18:35 Okay, so we're still only talking about instrumentation that our package is aware of, then?
**Jason Plumb** 18:42 I would say there's no other instrumentation. Like, if you don't implement Android instrumentation interface, then you're not instrumentation.
**Hanson** 18:49 Okay, got it, got it.
**Jason Plumb** 18:50 That's what I'm saying, yeah.
**Hanson** 18:52 Okay, okay, sorry, I think I was confused. I thought we were also trying to do, like, you drop a package, and that's not… doesn't conform to our interface. It gets picked up on the class path, just like what Java does.
**Jason Plumb** 19:04 No, I don't… I mean, we don't know anything about any of that.
**Hanson** 19:07 Okay.
**Jason Plumb** 19:07 Yeah.
**Hanson** 19:09 Okay.
**Jason Plumb** 19:09 There's plenty of other ways to get at the Android guts, and if someone's doing that and not conforming to our APIs, then that's outside the scope.
**Hanson** 19:17 Got it. Then… then… then definitely it should work, then I… yeah.
I think I was confused.
**Jason Plumb** 19:25 Main challenge is around the name of this DSL bit.
**Hanson** 19:30 Okay, well, just explicitly disabled.
Something like that.
Like, are you saying that suppressing just isn't strong enough? That it implies that it has to be a surface by default for it to be suppressed?
And you want something more explicit to say.
Anything included in this list will not be included regardless of whether it was enabled by the agent by default, or some other third party, or even you. If you include it explicitly, and you enable, and you include it in this list, this will also suppress it.
**Jason Plumb** 20:16 I mean, I thought it was a pretty reasonable name, but, you know, two of my other maintainers… Poked at it, so let's talk about it.
That's all.
**Cesar Munoz** 20:26 The… So, because given that all instrumentations have a name.
The only mechanism that we have in core to disable them is by… by name.
We said the name, and we… we go… in core and say, suppress… This instrumentation, and then we pass the name.
We are using that mechanism inside the DSL.
for the DSL API for the built-in instrumentations, which is the one that If you scroll down a little… Jason… There.
So, for example, we have this screen orientation instrumentation, which is… built into the agent, so we added this DSL config that, when you set enable false.
Underneath, it will suppress that instrumentation in core by name.
Now, what Jason is adding is, like, a direct way of suppressing instrumentation by names.
You know, without having to go through the DSL, because we don't know about those instrumentations.
in the agent.
It's just that… You know, from line… What happens on line 44 here, and what happens on line… 49.
it's… it's essentially the same. They both… End up getting suppressed.
Underneath in core.
It's just that what I was pointing out was that the one that we already have, it's… the term that we use, the verb, is enable.
false.
And then… The new one is suppressing.
So I thought that maybe it was confusing, because, I don't know, maybe a user will ask, what's the difference between disabling and suppressing an instrumentation, because for the ones that are built in, I disable them, but the others, I'm suppressing.
So… so… is it the same? And it is the same, so that's why I was… Pointing it out.
**Hanson** 22:41 And Jason, why… what was the point of contention of not just changing it to disabled, or something like that, to kind of have a… The parallel.
**Jason Plumb** 22:52 I just thought it read a little more fluent, and it avoids any… possible… Problem around saying disabled.
But, like, disable by name, or it's still verb-ish, right? And disabled by name, I guess, would be, you know, an option. If we like those, I can change it.
**Hanson** 23:16 So you do want a verb, then, or do you want…
**Jason Plumb** 23:19 Oh, I'm not, I'm not stuck on verb, no.
**Hanson** 23:21 Okay.
**Jason Plumb** 23:22 I want… I want what everyone likes.
**Cesar Munoz** 23:26 I could go with suppressed in the DSL one, it's just that we already marked it stable, so…
**Jason Plumb** 23:34 one, yeah.
**Cesar Munoz** 23:35 Yeah.
**Jason Plumb** 23:39 Yeah, I mean, I'm less… I think… I understand where Cesar's coming from, for sure. I'm less hung up… on the parallels between these two, because they're at different levels, and this one is addressing a collection, and this is addressing a singular one, and can go either way, right? It can go… True or false? And this one's explicitly, like, turn these off.
False, only.
So, yeah, probably, you know, if we want those to match, then it would be… if these are enabled, then these would be disabled.
And if it's important to call out that it only takes names, Then it's disabled by name.
**Hanson** 24:17 I think, to me, it's… whatever it is, is fine, as long as we document the correct behavior. Because if you say, say in this example, you go, screen orientation enabled true, but you go in suppressing or disabled by name, screen orientation, what the behavior there is. If we document that, then it… I… people should be able to figure out what they're dealing with. Like… The dealer…
**Jason Plumb** 24:50 is that we only have DSLs for the stuff that we force onto the class path, and we don't have DSLs for anything else, which is why this is, like, the bucket.
**Hanson** 24:58 Yeah, which is fine, because what we have is basically a shortcut, a list, and then also, you know, handles ones that we don't have a DSL for. So it's like, anything that's instrumentation, if it matches this list, it'll be disabled.
Or it will not surface, regardless of what the rest of the DSL says. It's like an overriding, deny list that you could set on, say, a particular app, and then even all the subsequent, configurations with different files, we'll have it disabled. But as long as that's well documented, I think… I think it's okay.
whatever name is okay. If you want the match, it's okay. If you don't want the match, it's okay. It is, by its very nature, not an instrumentation in and of itself. It's already different, right? Like, the rest of them are instrumentation names. You can figure this. This is like a one-off, hey, this is an overriding thing.
So, as far as people…
**Jason Plumb** 25:58 It sounds like… yeah, I didn't… I didn't sense any, concern around the approach or the structure. I think it was just almost purely around this word.
**Hanson** 26:07 Yeah, yeah. It… I don't have…
**Cesar Munoz** 26:12 I think they.
**Hanson** 26:13 I agree.
**Cesar Munoz** 26:13 Fine.
**Hanson** 26:15 Yeah.
**Jamie Lynch** 26:15 I think.
**Cesar Munoz** 26:16 It's fine.
**Jamie Lynch** 26:17 I feel okay with that word, like, after hearing… Always discussion.
**Jason Plumb** 26:23 Okay, to just call it suppressing or suppressed, what's better?
**Jamie Lynch** 26:31 I think… I'd be happy with Viva suppressing Feels okay, given that it's in… Well, it's within the instrumentation scope.
**Jason Plumb** 26:44 I think Cesar doesn't love it.
**Cesar Munoz** 26:48 The suppress versus suppressing.
**Jason Plumb** 26:52 Or suppressing it all, yeah.
**Cesar Munoz** 26:56 I'm… I get… I get your… the point. I just… I'm fine, it's just my thing is the intuitiveness of it.
Or the consistency.
But, I guess, you know, based on what Handsome said.
We can probably cover things up with docs, proper docs, and she'll be fine.
**Jamie Lynch** 27:24 Yeah.
**Cesar Munoz** 27:25 fine.
**Jamie Lynch** 27:26 We could also try something like ignore class path loading, or something along those lines.
That's a bit more explicit about what it's doing.
**Jason Plumb** 27:36 Do not load.
**Jamie Lynch** 27:38 Yeah.
**Hanson** 27:40 I think they're all gonna be fine, and especially because it's not a parallel property to enabled. It is something that's, like, already explicitly out of… it looks… it is something different. So, you know, nuke all, you know, it'll be like, what the hell is that? And you kind of look in the documentation.
After understanding intuitively a little bit. Okay, so if I new call, does that blow up if I explicitly set to enable? Yeah, it does, cool.
Whatever y'all pick, I'm good. I have my tiny, tiny preferences, but I don't.
ultimately care.
They're all good.
**Cesar Munoz** 28:24 I think… I think it's fine, then. We have the docs.
Suppressing, suppressed… Or suppress those three variants… variants at… I'm… I'm fine with that.
You know, I'll leave that, I mean, to whatever sounds best for a native English speaker person.
I, I think.
Because to me, they all, like, you know, they're all, they're all English.
So…
**Jason Plumb** 28:54 Well, the three people who were…
**Cesar Munoz** 28:55 Northern.
**Jason Plumb** 28:56 I don't know about Clever Trucker, David, but the three of us who have cameras on, who are native English speakers, all speak very different English.
**Hanson** 29:03 I'm not a native English speaker, by the way, that's my very second language.
**Jason Plumb** 29:06 Okay, okay.
Well, you wouldn't know that, Hanson.
You're very Canadian.
**Hanson** 29:13 Wait, are you saying I speak so well?
**Jason Plumb** 29:16 Yes.
**Hanson** 29:20 You maintainers decide.
**Jason Plumb** 29:30 Well, I mean, my instinct is to do the least amount of effort, so I would leave it the way it is unless someone has a preference.
I think suppressing is pretty clear. If someone were in the DSL and just, like, attempting to find the thing, maybe they would look for enabled or disabled first.
So maybe it's less obvious?
But I think we should make a decision.
**Cesar Munoz** 30:02 I think it's fine, we can leave it as is. I would like to add the docs, and probably mention in the docs, or maybe Maybe not.
that… I mean, the underlying mechanism is the same, so you can definitely suppress Built-in instrumentations, if you set the names there.
So if you know the name for the screen orientation instrumentation, you can definitely… Suppress it that way.
Or the older one, so… I don't think people should… I don't see why someone would want to do that, but… It will be possible, so…
**Hanson** 30:51 Go on, head out.
**Jason Plumb** 30:53 Yeah, yeah, okay, I just said that. Cool. You both have to dip, right? Yep.
Okay, well, sorry, I didn't get to the next thing, dang it. Okay.
Not a big deal. Have a good meeting.
Yeah.
**Cesar Munoz** 31:06 Yeah.
**Jason Plumb** 31:07 Yup.
Alright, so lots of bike shedding, I think we're just gonna keep it the same.
**Cesar Munoz** 31:13 That's the thing with naming.
**Jason Plumb** 31:30 Alright, and this has no approvals yet, I don't think.
Okay.
**Cesar Munoz** 31:34 Do you wanna add the, the dog changes?
**Jason Plumb** 31:40 Yeah, so where would the docs go? You mean in the repo somewhere? Like, what's the dock changes?
**Cesar Munoz** 31:48 I guess just, I was gonna say Javadocs.
**Jason Plumb** 31:55 God.
**Cesar Munoz** 31:56 A docs here.
**Jason Plumb** 31:57 Well, okay, so Javadoc's on which class or method?
**Cesar Munoz** 32:02 The.
**Jason Plumb** 32:03 In here…
**Cesar Munoz** 32:04 The… there, yeah.
**Jason Plumb** 32:09 Yeah, so there needs to be, like, a description of what this actually does. Okay.
Cool, I will take that as a follow-up item.
**Cesar Munoz** 32:28 Thank you.
**Jason Plumb** 32:35 Okay, so last time, we talked a little bit about maybe expanding the docs section on OpenTelemetry.io to include some recipes. You know, we have the sample app, and it's… I think we like it. The demo app is really helpful for, like, demonstrating what you can do with this thing.
And it shows most of the features, but not… maybe not all of them, and it's also maybe harder for some people. So, I think… We had discussed the idea of having a section in the docs.
about… platforms, client-side, Android, under here, probably as a sublist or something, or another page at least, which is, like, recipes, and the idea there was to say, like, oh, how do I do this thing? Like, I want to know how to do this thing, so almost like, Almost, like, little, just, like, snippets of, like.
DSL to show people how to.
**Cesar Munoz** 33:33 Ours.
**Jason Plumb** 33:34 Yeah. Almost like a fact, but like a how-to. And then… I didn't know what we wanted to start with. I don't want to just, like, blast a page of, like, 10 different how do I… so maybe I'll start with one or two, and I'm wondering what people think would be good ideas for that. So some that I came up with, and y'all can just tell me if you like or dislike any of these.
was like, how do I tell when the session changes? Like, people want that observer, that's a new change, right? We didn't have that in the DSL, but we do now.
Modifying the resource, using TLS, or sending a header. I didn't put TLS in here.
**Cesar Munoz** 34:18 The one that has come up.
**Jason Plumb** 34:19 So… Like this.
**Cesar Munoz** 34:23 There you go.
There's one that has come up a lot, and there seems to be a lot of confusion around it.
Excuse me.
Which is around adding… Global attributes that are dynamic.
it seems like… Yeah, it's…
**Jason Plumb** 34:44 Yeah, like, the user is a good one, right? Like, if the username changes, like, the user logs out and a different user logs in, they want that on all the telemetry.
Do we have that now?
Can you do that?
**Cesar Munoz** 34:56 Dynamic global attributes?
**Jason Plumb** 34:58 Yeah.
**Cesar Munoz** 34:59 Yeah, there is, I think you added that… that…
**Jason Plumb** 35:08 Sounds right.
**Cesar Munoz** 35:09 Sure. In fact, was that…
**Jason Plumb** 35:11 In the release notes, maybe?
**Cesar Munoz** 35:14 I don't know if it was… That reasons, but let me check.
**Jason Plumb** 35:18 Okay, here, this one… Yeah, February.
**Cesar Munoz** 35:23 That one, yes.
Oh yeah, it's fairly recent.
**Jason Plumb** 35:28 Yeah. Well, that's a good idea. So… like… Something like that.
**Cesar Munoz** 35:56 Yeah.
David's mentioning about aged custom HTV attributes.
**Jason Plumb** 36:10 Yeah, what's the mechanism for that? And, I don't know, does it have to be specific to OKHTTP?
These are… these are for client spans, presumably?
**Cesar Munoz** 36:23 I think so, yeah.
I'm curious if it has to be specific to OKCDP, because I'm… I'm guessing Clients.
will want just HTTP attributes, whatever, you know, underlying mechanism creates them.
**Jason Plumb** 36:42 Yeah, and have we added a way… I think there was some talk about span processors, have we added that yet?
**Cesar Munoz** 36:52 No, we haven't.
I asked about the use cases in the issue that someone created for it.
But I think we haven't gotten an answer.
Because, apparently, their use case was fixable with the new dynamic global attributes.
**Jason Plumb** 37:13 Oh, yeah, okay.
I like supporting Span Processor.
Just because it feels a little more open telemetry-ish than global attributes.
But…
**Cesar Munoz** 37:31 Yeah, it definitely got benefits. I think a good thing about supporting processors is that you get the, The… the… the signal, with all of its… Existing attributes and everything, and probably that will help you make a decision on what kind of attribute do you want to add? Because it's like, the, let's say that you want to add attributes to all of the HTTP spans, but then for… for you to do so, you will have to know which span you know, belongs to an HTTP request.
And then, for that, I think the only way you can do so is By checking the attributes.
So… Well, it's like a global way to do so.
**Jason Plumb** 38:19 Yeah.
**Cesar Munoz** 38:20 So… Yeah, I guess we can go with custom processors.
**Jason Plumb** 38:29 But I think we don't have that built yet.
**Cesar Munoz** 38:32 No.
**Jason Plumb** 38:33 So that would not be a shortlist for documenting if it doesn't exist yet.
**Cesar Munoz** 38:39 Correct.
I was waiting for that… A use case that needs it, both.
**Jason Plumb** 38:47 Yeah, yeah.
So if we wanted to customize… Yeah, so today, what's the mechanism today for customizing HTV client spans.
Like, David, you brought this up, but I'm not exactly sure what the mechanism is, at least not off the top of my head. Like, if I wanted to only add an attribute to HTTP client spans, how could I do that using the agent?
And maybe we can't.
Yet.
It's good food for thought.
Okay, well, it might take me a day or two to kind of get this bootstrapped into a PR. So if you have other ideas, feel free to add them here.
**Cesar Munoz** 39:49 But I think it's a nice start.
Quite a lot of useful things there.
Yeah, I wonder if I should…
**Jason Plumb** 39:56 I wonder if I should create an issue on the I.O. site for it. I never go there.
Do we have anything that's, like, Android?
We do.
And, oh, there's a SIG tag!
Okay, I will create… I will create an issue… That way we can have a list to refer back to.
And then, we can check them off as we build them.
Sound good.
**Cesar Munoz** 40:45 Sounds good.
**Jason Plumb** 40:47 Cool.
Well, I don't think in the last day or so that there have been any new issues.
Compared to you.
**Cesar Munoz** 40:58 So right now, I knew there was something, but it's only for OKCP.
The, what is it?
**Jason Plumb** 41:05 Yeah, this thing.
**Cesar Munoz** 41:07 I just sent the, the instrumentation has a couple of configurable parameters.
And one of them is about adding attributes.
But, it's… it's okay HTTP specific, and… It should be fixable by allowing a custom processor.
Which I think is ideal.
So…
**Jason Plumb** 41:39 Yeah, there's no… but this is not exposed through the DSL yet, through the agent.
Right?
**Cesar Munoz** 41:45 Yeah, no, no, because this is not even in the agent.
are built in.
**Jason Plumb** 41:50 Right.
Okay.
**Cesar Munoz** 41:56 It's configurable, but it's tricky to find, and probably cumbersome, so… and it's only okay to be specific.
**Jason Plumb** 42:05 So let's talk about this one.
Yeah.
Yeah, so this, this is a feature creep.
And… I haven't seen these yet.
Yo.
**DavidGrath** 42:33 Okay, how's not the police, I like clear items, man.
**Jason Plumb** 42:44 David, I feel like your audio's pretty muffled.
**DavidGrath** 42:56 Okay, this is a hell.
**Jason Plumb** 43:01 I think that got a little better, maybe.
**DavidGrath** 43:04 Okay. So the commit I recently made, actually, yeah, I made a new commit, actually. So I removed the line 32, and instead, I added it to the… settings griddle as… as I was instructed, but then I also added Azure Instru instrumentation into the settings griddle as… into the… into the beautiful gridophile as well, because… the IDE complained about the superinterface missing… being missing, rather.
**Jason Plumb** 43:33 So, so this is, this is good. I mean, I think it does need to be in the build gradle for the demo app.
And not for the agents.
So I think that was the change that… Like, originally there was this change, right? So this is in the agent Gradle, and we… I think this is what we don't want.
I think we should remove this one.
Does that make sense?
**DavidGrath** 43:56 Okay, yeah. Yeah, I already did that, yeah.
**Jason Plumb** 44:00 Well, it's so sweet.
It's still showing up here for me. Yeah, if we just click into the PR, it's still there.
**DavidGrath** 44:09 Okay, I gotta chuck it again.
**Jason Plumb** 44:11 Okay.
**Cesar Munoz** 44:13 But I think, if I understood correctly, probably.
David was getting issues with the… Let it… The independent dependency not found in the demo app, probably because of the changes in settings… in the settings cradle file.
That we're needing.
So…
**Jason Plumb** 44:36 Oh, yeah.
**Cesar Munoz** 44:38 Understood correctly, yeah.
**Jason Plumb** 44:39 No, I hate this so much, yeah, yeah, okay, now I'm caught up, yeah, okay, so this is a pain in the ass, but yes.
Yeah, these are required. So once you have these in place, you can include them like this, and then you can remove it from here. Yeah, it just sounds like you're very close.
**Cesar Munoz** 44:56 But by the way, just wanted to clarify, if someone's watching this.
for other use cases. That change in the settings cradle file, it's only in this project's demo app.
Because the demo app is part of the… same project that creates the agents, so there's a compilation Ordering that has to happen there, and yeah, it's a bit ugly, but it's not something, like, people in their projects will have to do.
**Jason Plumb** 45:27 Exactly, yeah, it's good… it's a good clarification for the recording, at least, or any transcriptions that might be coming out of this. Yeah, these substitutions only are required because the demo app is within the same repo, and we want these to be live, like, stitched to the live code.
and not through Maven dependency on Maven Central or something. And when this… when this moves, when the demo app moves to the demo… the OpenTelemetry demo project.
These will go away, and these'll just… it'll just be a Maven dependency then.
And it will… it'll lag a… it'll lag a month behind.
**Cesar Munoz** 46:02 Another reason why it's nice to move this to the, hotel demo project.
**Jason Plumb** 46:08 Yeah, because it's closer to what people will be using and actually seeing.
**Cesar Munoz** 46:12 Yeah.
**Jason Plumb** 46:13 Yeah. Do we have an issue for that yet?
**Cesar Munoz** 46:18 I think we're doing.
Sorry.
**Jason Plumb** 46:28 I think we should create one.
**Cesar Munoz** 46:31 I remember you mentioning it a couple of weeks ago.
**Jason Plumb** 46:38 Not to move it, to create an issue to move it.
Okay, I'll at least create a tracking issue so we don't forget about it.
**Cesar Munoz** 46:53 Got it. I probably can take a look at that.
**Jason Plumb** 47:00 Sounds good.
**Cesar Munoz** 47:01 moving it. The idea will be… well, we can discuss it in the issue, but the idea will be to move it not copy it, right? It's like, moving it, so removing it from here.
**Jason Plumb** 47:12 Yeah, I mean, I think it'll be a… it'll be a large donation, or, like, a migrate little… it'll… it'll be a huge addition to that repo, and once it gets merged, we can delete it from ours.
**Cesar Munoz** 47:22 Got it.
**Jason Plumb** 47:23 So I think there will be some… some brief period of time where the code exists in two places.
But then we should… we should really make a point of deleting it from ours so that we can… not have to maintain two codebases. I also don't want it to seem… we have to figure out what it means to have that code over there, because… we should help maintain it, right? Like, right now, we're on the hook, and we maintain the demo app as part of our repo. When it goes over to the demo app, we're also… we should be on the hook.
For helping maintain that, but I don't know what the ownership model is like over there, because that's a pretty big project.
And I think they've only got, like, a few maintainers. But yeah, look at that, ContribList is huge.
Yeah, well, they've got a reasonable staff, but I don't know, you know, this… the Android demo is not tiny.
But they were stoked about it when we demoed it, like, 2 years ago or whatever, so… or a year ago, whenever that was.
Yeah, I'll take an item to add that as an issue, and we can… Find time for it.
**Cesar Munoz** 48:31 Yeah, thank you.
**Jason Plumb** 48:32 Yep.
There was someone who was really struggling, I think there was a PR… Yeah, this PR… They're really struggling with the, easy CLA.
I think they haven't… oh, wait, what's this?
Oh, it's still messed up.
**Cesar Munoz** 48:57 I was, reading your comments, it's probably because of the signed comet… comets?
Particular comment? You think that…
**Jason Plumb** 49:06 Yeah, signed commits. Do you think that that's blocking the CLA?
**Cesar Munoz** 49:11 But CLA, for me, is a black box.
**Jason Plumb** 49:14 Yeah.
I mean, and if I try and get more details on this, it's just like… It's asking me to sign this, or whatever.
This is not good.
There it is.
like, I've… I mean, I signed the… I signed the OpenTelemptry CLA many years ago.
But that's… when I do details, this is what it's asking me to do. I'm assuming that I haven't… I haven't gone through this process in some time, but I think… I think that this is what the PR submitter also sees.
But, yeah, I was hoping…
**Cesar Munoz** 49:54 They say they'll already… Went through it.
**Jason Plumb** 49:57 They said they clicked through the EZCLA, yeah, they said that.
And here was the email confirmation, that's cool, but to fix it, I was like.
Maybe redo the commits with signing, but this is not signed.
I'm assuming.
How can you tell if a commit is… I thought that there was a marker next to these… Let me pick a different PR.
**Cesar Munoz** 50:31 Go to the… Comments, commits, list.
**Jason Plumb** 50:37 Oh, is that where it is?
I think this is…
**Cesar Munoz** 50:39 Dave.
**Jason Plumb** 50:44 I thought it used to show that. Oh, is it this?
Yeah, those are checks.
These are the checks, like, the verifications.
**Cesar Munoz** 50:59 Yeah, I don't know, it's confusing to me as well.
**Jason Plumb** 51:01 I know, how can you tell? I thought there was an indication, but maybe I'm just thinking of this, but that's checks, I think.
**Cesar Munoz** 51:11 I remember seeing somewhere… a while ago.
That the, the… when the comment was signed.
But.
**DavidGrath** 51:21 I thought that EZCLE… oh, sorry. I thought that EZCLE check. Didn't you overlook it just now?
**Jason Plumb** 51:30 Say it one more time, David?
**DavidGrath** 51:33 Yeah, but I thought… isn't that the sign… The same, what are the colors.
The signing indicator is different.
**Jason Plumb** 51:43 Yeah, there's two different things. There's the sign commits, and there's the easy CLA. Those are different things.
**DavidGrath** 51:49 Okay then. That's it.
**Cesar Munoz** 51:50 And probably ECCLA doesn't take into account design commits, because I just sent a link to a PR of mine, and I think that's… You can see there how sign committees.
**Jason Plumb** 52:03 Verified. Yeah, verified, okay.
**Cesar Munoz** 52:07 So…
**Jason Plumb** 52:09 But, like, in David's PR, we've had work David submitted work to us before, I think, and… This is not showing verified, which is weird.
**Cesar Munoz** 52:20 But CLA is still green, so probably it's not related then.
**Jason Plumb** 52:23 So maybe we don't actually require assigned commits.
Huh.
**Cesar Munoz** 52:30 Maybe it's a new thing that comes.
**Jason Plumb** 52:32 No, this could be a… this could be a JSON problem, because we do, at least in Splunk, we require signed commits, and so maybe… Maybe I was assuming… that that was a requirement, because I put something in the contributing as well, so maybe that's wrong. Maybe I screwed it up.
**Cesar Munoz** 52:53 I don't know. I mean, I wouldn't be surprised if that's added to… CNCF.
To the hotel community?
**Jason Plumb** 53:02 I mean, yeah, I would expect them to want that, but, like, we clearly don't have that. Like, let's just pick another random old PR that's closed.
Especially if we can find someone who's not, like, a core contributor, like… Like, who's this? Like, this one.
Right?
Does that show verified? It does not.
So, I think we should pull that back out. I think I was mistaken. I think we don't actually require signed commits.
**Cesar Munoz** 53:35 It doesn't look like it. I do, I'm also confused, because… we do the same requirement in Elastic. That's why mine is verified.
Yeah, me too.
**Jason Plumb** 53:47 It's there, yeah, yeah.
Okay.
Well, that's good. I mean, so I just need to… I'll take another action item to revert the damn signed… Alright.
Humans are also prone to hallucinating.
**Cesar Munoz** 54:14 It's confusing. I've seen a couple of results searching for sign commit in the hotel Slack.
But, yeah.
probably it is requiring some repos… yeah, I don't know.
**Jason Plumb** 54:33 Well, I also feel bad for this person, because I'm telling them to, like, turn on signed commits when it's totally not a thing.
I just…
**Cesar Munoz** 54:40 But again, it's confusing that they say that they went through the CLA Stuff, and it's still not green then.
**Jason Plumb** 54:47 Yeah, so it's something else, and I, you know, this… I thought this worked, but it completely did nothing… Yeah, maybe I'll… maybe I'll see if someone on the… TC can help out here, because I don't… I don't know.
It'd be cool to get that unblocked.
**Cesar Munoz** 55:11 Yeah.
**Jason Plumb** 55:16 Yeah.
Okay, well… I have some action items to take away. Is there anything else that people want to talk about in the couple minutes remaining?
Okay.
Well, we certainly appreciate all the help, everyone.
And we'll see you soon in the comments, and then we'll be back in SIG next week.
**Cesar Munoz** 55:45 Yeah, bye. Thank you.
**Jason Plumb** 55:47 Yep.
