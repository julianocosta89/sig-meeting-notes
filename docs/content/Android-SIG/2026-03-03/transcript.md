SIG: Android SIG
Date: 2026-03-03
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:23 Hello.
**Manoel Neto** 00:26 Hello, hello.
**Jason Plumb** 00:34 Let me pull up the doc…
Oh, we got a bunch of topics already, alright.
**Hanson** 00:49 Where are you guys? There we go.
**Jason Plumb** 00:52 We are.
**Hanson** 00:53 June?
Good morning.
**Jason Plumb** 00:57 Morning, afternoon?
Good day.
**Hanson** 01:03 There you go.
So, British Columbia is getting rid of daylight savings, or staying on daylight savings.
**Jason Plumb** 01:15 lucky.
**Hanson** 01:17 Yeah, we're gonna be out of sync with frickin' you guys and California, so it's gonna be annoying as shit.
**Jason Plumb** 01:23 Yeah.
Yeah, we… we passed a, state thing, but there's… it's, like, contingent on, I think, Washington and California also doing it. So, if they… if we all agree, then it will happen. If, you know, they don't, then it won't, and…
Good luck getting Washington to do it.
**Hanson** 01:42 Is Washington the holdout? I thought California would be the holdout. I mean, it might be both of them at this point.
But it's gonna be so confusing with, with Argentina and as well as the UK, when I can't just say, hey, like the rest of California, I'm switching. It's like, no, I'm not switching, so…
**Jason Plumb** 02:03 Right.
**Hanson** 02:05 I'm not Pacific time anymore, I'm fucking British Columbia time, or whatever, I don't fucking know.
**Jason Plumb** 02:10 When does it happen? Is this the first year?
**Hanson** 02:12 we switch for Daylight Savings in… in, like, next week, and then I think we stay on there.
You know, so when they switch back…
**Jason Plumb** 02:21 Yeah, so we're gonna spring ahead, and so this is make… it'll effectively make this meeting an hour earlier for you?
**Hanson** 02:27 Fuck.
**Jason Plumb** 02:28 I, I think…
I think is the way that works, right? Because we're gonna bump the clocks up from 7 to 8, or from 8 to 9, right? So…
You're gonna stay back, yeah, I know.
**Hanson** 02:41 I gotta do the math, if football starts at 6 AM, that's gonna be horrible.
**Jason Plumb** 02:45 But I guess it raises the… I guess it raises the question, like, this meeting is set up for Pacific time?
Like, it… does it follow a time zone? I don't even know.
**Hanson** 02:56 So, Manuel, where you are, you have daylight savings, right?
**Manoel Neto** 03:01 Yes.
We do.
**Hanson** 03:04 Cesar, Spain has that as well.
**Cesar Munoz** 03:07 Yep.
**Manoel Neto** 03:10 So… It's always a debate, so… at some point it would change, I guess. Also, it's always against the rest of the EU, not…
**Hanson** 03:17 I feel like most people are on a switching schedule, so it kind of makes sense. You know, those of us who are, you know, pinned to a time, that's when…
Those are the ones we're gonna have to switch, so…
**Jason Plumb** 03:32 Alright, so it's next week.
Or is it… no, it's this… it's this coming weekend. Okay.
Alright.
Well, that'll be exciting. I'm sure nothing will go wrong.
**Hanson** 03:47 Yeah, when does British summertime start?
Not next week, right?
**Jamie Lynch** 03:54 Yeah, it's the end of the month.
I hate…
**Hanson** 03:59 I hate it.
Alright. Okay, more flexible.
**Jason Plumb** 04:06 We have some good attendance now. Let's look at this first issue. Thank you for putting agenda items in ahead of time.
Let's talk about bumping the min Kotlin version.
**Cesar Munoz** 04:22 Yeah, I added the… their… Sorry, I'm feeling a bit under the weather today.
I added it there, but it's mostly something that I think was Jamie who brought up.
which, you know, it's… I guess, in a summary, it's,
If we should bump the minimum version of Kotlin.
That will probably cause some breaking changes, or…
That… I don't remember the details.
maybe… Jamie, if you remember.
Sir?
**Jamie Lynch** 04:59 Yeah, so… I think… I can't remember what we're commonly building with, I think we're commonly building with…
2.2, and that gives support back to 1.8.
Whereas the latest version of Kotlin.
2.3 if we only allow… if we only build with that, I think.
Yeah, support's back to… 2.0… Incompatibility, and 1.9 with a deprecation warning.
So… Yeah, this is one of those things that, Kotlin only supports will last for
Like, version bumps, the last four minor version bumps.
so, we'll continue to get ratcheted up, basically, with our versions.
**Hanson** 06:02 Basically, that's.
**Jason Plumb** 06:03 That's for compilation… that's for compilation targets.
Is that what that means? Because when I look at… when I look at this, right, this is the version that's being used, for compiling.
It's also… it's also… Assumed that, there's a different version that it's targeting.
And that… and that has to be compatible with whatever the runtime version is, right, of the standard library.
So if someone… if someone uses this, like, if we… if we merge this, and someone uses…
Sorry, if someone uses our build, that comes as a result of us having merged this.
then what they get is something that cannot be run on Kotlin 1.8.
Is that… am I understanding that correctly? Yeah.
**Jamie Lynch** 06:53 Yeah, that's.
**Jason Plumb** 06:56 So the question is, do users…
Requ- like, our users who are actively…
updating dependencies and rebuilding with our library, are they using Kotlin 1.8?
And I don't think we have a way to answer that, so we have to assume… Probably yes.
Which means what? That this is a breaking change for those people, right?
**Manoel Neto** 07:24 Yes.
It is… I'm not sure…
if you can actually do anything else, because, like, for example, today you cannot even use the latest versions of Flutter if you're not using Kotlin at least 2.0 already, so all the tooling is already migrating for the latest versions.
So… It is a breaking change, it is a minor.
**Hanson** 07:46 But I don't think there's any other way.
**Manoel Neto** 07:49 You cannot keep compatibility, because at some point, you cannot even upgrade the Android X libraries, you cannot upgrade anything else.
**Jason Plumb** 07:55 Right.
**Hanson** 07:56 The problem is we are being squeezed, so, without updating, we aren't able to support
So I believe we are… compiling down to 1.8 right now for, compatibility. So,
with that version of Kotlin compatibility, you cannot use, Kotlin 2.3 at runtime, to, or even at build time, when you target 2.3.
To compile, because it just doesn't understand, you know, those old versions.
So, as it stands, I don't think that somebody could use Kotlin 2.3 at runtime with our SDK. And I believe Jamie's PR will fix that.
So, we know people will want to use Kotlin 2.3, because it's recommended to use the latest runtime, even.
**Jason Plumb** 08:59 Yeah, sure.
**Hanson** 08:59 compatibility is at a lower version.
the ones who are not upgrading from 1.8 likely are using, like, a very old version of something like React, or Unity, or Flutter that forces, or that brings in an older version.
So those are unlikely to be using the latest, you know, OpenSumptu SDKs anyway.
So, it's probably safe, but, you know, it is… it is a breaking change, but it's one of those changes where we're gonna have to…
do this type every time Kotlin releases. So I don't know if it's a major version bump for us, even though it's a breaking change, especially if it's, like, a…
a change where you could… you could just upgrade, your Kotlin runtime and be fine.
So… You should do it.
**Cesar Munoz** 09:57 Yeah, I think we can also follow what they do in OKHTTP, which is…
If somebody asks them, because we have already done so.
to support an older version of Kotlin.
they just go and say, well, you just then have to use an older version of OKHTTP if you want to use an older version of Kotlin, so…
It's what it is, and I think it will be more work for us to try and battle that.
you know… That fight, because it's like… It seems to me that
there's a chain of, I don't know.
things are going on in Android.
That kind of force… developers to always stay updated with the latest versions of everything, so…
I don't think we should fight that.
So yeah.
**Jason Plumb** 10:56 Yeah, so I'm inclined to say we do not bump major version for this, and we just call it out in the release as a breaking change.
And maybe we put a little footnote that says, if you need to stay on Kotlin 1.8, you should not upgrade.
I mean.
**Cesar Munoz** 11:13 That sounds good.
**Jason Plumb** 11:14 That's the unfortunate reality, is like, yeah, the ecosystem is moving forward, and…
You know, if you wanna… if you wanna stay with us, and you need to upgrade, and if not, you can stay with the previous version.
Yeah, I think that's… I think that's the way I'd like to handle it right now.
Just to make sure we have a… just a breaking change in the… in the changelog for the release notes.
And just call it out like this.
**Hanson** 11:40 If we don't have it, we can also have, like, a compatibility statement in terms of, like, you know, indirect compatibility, version compatibility, things like AGP and things like that, because, you know, that stuff is also going to move, without major versions moving. So we could basically state that, hey.
sometimes these will have to be moved because the platform dictates it, or, you know, whatever reason. And changing AGP versions won't necessarily upgrade… bump major versions, but it will be called out.
**Jason Plumb** 12:14 Yeah, I mean, unfortunately, reading this, if we're pedantic.
These versions, meaning referring to these, right, can be bumped in a major version, ugh, when one of these three things happens, and this second thing is what's happening, right?
At the discretion of us. So…
You know, it's any three of these.
**Hanson** 12:38 But it does call out major version. Now, you know, we're not… we own this document, we're not beholden to it.
**Jason Plumb** 12:44 So… If we decide to do it, let's just… we could just change this and remove that.
**Hanson** 12:52 We're not stable yet, right?
**Jason Plumb** 12:55 Go ahead.
**Hanson** 12:55 We're not stable yet, right? Is that… can we still… no, we can't say that anymore. Dammit.
**Jason Plumb** 13:00 I mean, we're 1.2 now, so, I mean, we want to try and not have breaking changes.
Technically, what we declared was that our API is stable at the agent level, and nothing else yet is.
So maybe we should walk this back a little bit, and just revise this to say these versions can be bumped.
when, or bumped in a release as a breaking change, when, and then call these three things out. Because it, I mean…
I think it makes sense to have language in there that says, yes, there will be breaking changes for versions of these dependencies, because the ecosystem moves pretty fast.
**Manoel Neto** 13:42 Which is fun to say, thinking about the driveways, the ecosystem.
**Jason Plumb** 13:45 Say again.
**Manoel Neto** 13:46 Yes.
**Jason Plumb** 13:47 What's that?
**Manoel Neto** 13:48 Which is funny to say that the Android ecosystem moves fast.
**Jason Plumb** 13:52 Well, I mean, I also work on Java, where we've still got Java 8. I mean, and every time I bring up the idea, even, of dropping support for Java 8, which a lot of libraries are doing now.
It just scoffs all around. We can't drop support for Java 8! Never! So, this moves a lot faster than…
Java, I suppose.
What do you think, Jamie, about making that change as part of your PR, and also including an item in the changelog? Can you do those two things?
**Jamie Lynch** 14:28 Yeah, I'm happy to… kind of tweak.
the wording we were using there. And I can add something into the changelog about this.
**Jason Plumb** 14:38 Okay, I think… I think if you do that, I'm happy to merge this. I mean, I was already pretty… pretty close on it, but I think…
Given this discussion, we should probably do those two things, so…
**Jamie Lynch** 14:49 Cool.
**Jason Plumb** 14:51 I think we're there, as far as approvals go.
Oh, now we've got merge conflicts, hooray!
Well, we've definitely got the approvals, but given this conversation, I think it would be nice to have
Breaking change called out in the changelog.
And just, like, tweak the wording and versioning.
Sweet.
**Hanson** 15:37 Anyway, I posted, a link under that topic, if you want to read a blog post about
various, versions of Kotlin and what it means,
Compile, runtime, target, standard… standard library, da-da-da-da-da, so…
**Jason Plumb** 15:57 Yep.
Okay, cool.
We ready to move on?
Okay, sounds like it.
Animal sniffer.
**Cesar Munoz** 16:14 Yeah, so I was testing with an ancient Android OS last week.
And I realized that, it's, it's, crashing because of a class not found.
That it's currently used in disk buffering.
Now, the thing is that it was strange, because…
the class that is being used in this buffering didn't get flagged as, you know, unsupported by Android 21.
And… That goes back to this… You know, animal sniffer check.
That it's supposed to, you know, tell you that you're using classes are not available.
in that version of Android.
So, the failed check… the… sorry, the check failed.
And I started to dig why, and essentially.
I took a look at the Google's tool. So, just for context, So, okay.
Yeah, I should provide some context. So, the, so we have…
a minimum supported version of Android API 21.
But the only way that users can, you know.
execute Autel Android in an API 21 is by using
the, the sugaring tool that Google created.
What the distributoring tool does is, essentially, in a nutshell, it's just… it adds all of the JDK classes that are missing in the… in that old version of the OS. It adds it into your application.
And then it changes all of the references to that class… to those classes within your application.
to the new, you know, place in your application. Something like that. I hope it makes sense. Essentially, just…
It covers the gap by adding all the stuff that's missing.
Into your app.
**Jason Plumb** 18:11 The problem is that…
**Cesar Munoz** 18:13 So, what Alamar Sniffer does is that it checks
The sugar and lip, which is the one containing all of the missing classes.
It checks all what's in there, in that jar file, And…
Everything that it's in there, it marks it as safe to use.
Because it's in the jar.
The problem is that it turns out that that's not the case for some classes. It seems like there are some exceptions, that even though they are
Available in the JAR file that Google provides.
They're still not… Processed at compile time.
So that, you know, they're replaced.
So… Some of the exceptions… well, the exception that I found out was the completable future.
class.
So I asked an AI to check for the rest, because it's a huge project.
And apparently these… all of the stuff that is there quoted are the exceptional classes.
So essentially, those won't get flagged.
By animal sniffer, but still, they will cause a crash.
If we use them. So… I agree with this issue in the… Repo that creates the,
the signature that we use to verify with Animal Sniffer. I haven't gotten an answer yet.
There are many things that we can discuss here, but essentially…
regarding this issue specifically, I think we have two options.
One, we just fix this in this buffering and avoid using completable future.
That way, we keep… you know, the functionality intact with API 21.
Or two, we raise the minimum SDK version to use OZLandri to 24.
Which is a minimum… which is the API where this class is… is available.
So that's what I wanted to discuss here.
Because after discussing this, internally, and with other people I know, Android developers.
It seems like they don't quite understand why somebody will use API 21.
nowadays, so… That's why I wanted to discuss here.
**Jason Plumb** 20:39 So we do use Animal Sniffer on the disk buffering project as well. Okay, so it has to get through this first, and then it also has to get through the Android one?
Meaning, get through this, by that I mean, it has to pass the check that exists in contribib, and then we also have a check, right? In Android?
**Cesar Munoz** 21:01 We do, but it's essentially the same check, so it's gonna fail in both places.
**Jason Plumb** 21:05 It is, but it's via dependency in this case, right? It's not a direct usage.
**Cesar Munoz** 21:09 Yeah.
**Jason Plumb** 21:13 Okay.
**Manoel Neto** 21:13 David.
**Jason Plumb** 21:14 Go ahead.
**Manoel Neto** 21:15 I think all the Android X libraries are already required, the minimum SDK 23 or more, so from 21 to 23, we can just do it, because I don't think there is any Android app today without Android X libraries anyway.
**Hanson** 21:32 Yeah, I believe we talked about bumping this, last year sometime, that the use cases for 21 exist, but is, very small and, and, you know, at the same time.
we… those who use the SDK, we don't dictate what they want to support, or who they want to support,
But that being said, similar to the Kotlin version, it's like, you could use the old, version if we really, really want to use it, and wanted to support 21. So,
I think bumping it makes sense, even regardless of,
the, whether it's needed in disbuffering or something else. I mean, I guess also those, you know, not using Java will make this go away, just because Java usage is…
just iffy, for Android anyway, but, you know, that's neither here nor there. That's, like, almost a separate thing. So, I think I'm happy with… with…
Any of that, in fact, if we want to do…
So play is 23, so I think up to 23 is pretty safe.
But, if we need completable future in 24, that means we have to go 24.
And then, why not go 26? You know, it's, it's where do we stop, kind of thing.
So, it's either choosing between 24, or… which means we can use completable future, but we still have, you know, potentials of the other ones sneaking in. So, you know…
I don't know how we guard that. Maybe we don't, because we just… new code just won't be written in Java, so we don't worry about it.
**Cesar Munoz** 23:28 Yeah.
In an ideal world, I think 26 would be the greatest option to go with.
Because my understanding is that API 26 is the one that
is the most pair with Java 8.
Which is the version of Java used by Autel Java.
So… It's really the… like, if you have an Android.
device with API 26, you don't need
To do any kind of, you know, de-sugaring or any of these shenanigans.
It's only for APIs below 26.
Now, 26, I think it's quite high.
Unfortunately.
So… Yeah, I would say probably 24…
If we go with 23, just to keep in pair with Andri X, as Manuel mentioned.
then we'll still have to, update this buffering. And not only this buffering, we should, like.
Find a way to make sure that these
Exceptional types don't… don't sneak into… into the code from now on, until we reach Either API 24, or…
Until we switch from… Autel Java as a base to Autel Kotlin.
Which should make these issues go away.
**Jason Plumb** 25:00 Yeah. So, yeah.
**Hanson** 25:03 Yeah, there's probably, like, 3 distinct problems we… we could…
solve with a combination of these things. One is the obvious problem right now with the communal future for, for disk buffering. That's one. Two is raising minimum versions, period, in order to
drop support for older ones. And then 3 is, as you said, the,
picking up, other violations.
I think pick up other violations…
I think it's not worth the squeeze at this point.
Because, I'm hopeful that most of the stuff that we write going forward will be in Kotlin, and we don't have to worry about that. So the actual Android project, we wouldn't have to worry about that. And the only dependencies that we pull in from, that is critical is,
the, disk buffering, and…
I don't know if all that worked just to make sure disbuffering is free of that in a programmatic way that we could detect. I don't know if that's worth it. So, really, for me, it's… do we bump it to 24 and not have to worry about this?
Or do we fix, a completable future and not have to worry about this?
**Cesar Munoz** 26:29 In order to make sure that this won't happen again, I think we have two options.
That whoever is maintaining this library can…
Update it, so that it accounts for those exceptions.
Or the second one, which I find it quite unlikely to happen, is to add into the contribo
some Andre emulator tests.
For this buffering.
I'm not sure if that's gonna happen, because it's, you know, the contract repo is not an Android-specific repo, but it could be a way. And we should also have to do the same in our repo.
Where we test with an Android emulator of API 21.
Which, that's… doable. But I'm concerned about this buffering.
**Hanson** 27:22 Another option is have a lit rule, and include all the classes that you found, and say these are forbidden.
**Jason Plumb** 27:30 So, I was… I wanted to ask about that, so…
Why… remind me again, I think you already said it, I'm sorry, I'm still waking up here, why… why didn't Animal Sniffer catch the fact that completable future isn't compatible?
**Cesar Munoz** 27:44 Because it's in the jar file.
That contains all of these missing classes.
The problem is that, if you scroll down to the last part of that quote.
**Jason Plumb** 27:54 Yeah.
**Cesar Munoz** 27:54 last paragraph. It says, the reason these classes are in the source but not the sugar seems to be that they serve as internal dependencies for the classes that are the sugar. So, for example, concurrent HashMap uses forkjoint port.
**Jason Plumb** 28:08 Hmm.
**Cesar Munoz** 28:08 like that.
But the compiler just…
**Jason Plumb** 28:11 They're only… they're only included in the jar because they're depended on by other safe…
Yeah. Back portable… okay, de-sugarable.
**Cesar Munoz** 28:20 According to these, yeah.
**Jason Plumb** 28:22 Interesting, okay.
So there's… that leaves a window for stuff to get through, and this is just one example.
There's a bunch of examples on screen here, but we… I mean, you bumped into Completable Future, right?
**Cesar Munoz** 28:35 Yeah.
**Jason Plumb** 28:37 So I was looking at… you know, there's a comment in this class, which is in the core Java repo.
Because completable future, I think, does not exist in Java 8.
**Cesar Munoz** 28:50 Got it. Or maybe it… maybe it does, but…
**Jason Plumb** 28:55 I forget, but I think this… I think this was created to kind of mitigate some of the issues around this, like…
**Hanson** 29:04 Oh.
**Cesar Munoz** 29:05 came in, but, you know, we could consider doing something similar…
**Jason Plumb** 29:11 I don't love it.
But I'm just calling this out as an option.
**Cesar Munoz** 29:17 We can reuse this class.
In country.
**Jason Plumb** 29:21 Yeah, depending on the types that we're putting in the future, right? Because this is just a code, you know?
But maybe we can. I mean, those features usually get used for, like, an asynchronous success, like, pass-fail kind of thing.
**Hanson** 29:36 The safest thing, or the smallest change, is just to fix that, and then we could, bump the min version separately later on, when we have, like, a really super compelling need.
**Jason Plumb** 29:48 When you're saying, fix that, what do you mean? Don't use completable future.
**Hanson** 29:51 Don't use computable futures, so basically kick this down the… kick this can down the road, and not be comprehensive, because,
like, I feel like the number of Java things that we're going to depend on is going to be, you know, dwindling, this being, like, a major one, but I would say that it's not like we're getting, like, a change every week here. So.
**Jason Plumb** 30:15 I keep coming back to this, you know, 26, we're almost at 95% of the market.
Right? Like…
**Hanson** 30:24 Yep.
**Jason Plumb** 30:25 It's pre… and it's, you know, it was born in the year that predates the OpenTelemetry project.
You know, that's… Another way of looking at it.
**Hanson** 30:36 So, I think bumping it, will… you'll only cause certain people consternation who are, you know, either a really big app that still has, like, super minimum version, or a really small app in an enterprise where they support, like, really old versions.
So it's not going to be a mainstream use case. In fact, if you go to Google Play, they don't even give you data now on anything below Android 10.
**Jason Plumb** 31:04 So if you have crashes below Android 10, you don't see them in Google, Google Play, when it was last updated.
**Hanson** 31:12 So, I think, especially if there aren't, like, you know, salespeople breathing down our necks and say, hey, why did this change? We can totally do that. I would say, though, if we bump… if we get rid of that many versions,
It may be a major ver- .
**Jason Plumb** 31:32 You mean from 21 to 26? Yeah, that feels…
**Hanson** 31:34 Yeah.
**Jason Plumb** 31:35 Yeah, I agree.
**Cesar Munoz** 31:39 Okay, I'll create a PR for this buffering.
And, I'll… I keep an eye on this issue to see if the maintainer comes back.
And, I'll probably add some Android 21 tests to… to RCI.
Just to make sure.
**Hanson** 32:01 There, I think there are, but I don't know if discount buffering was enabled.
**Jason Plumb** 32:04 Right, yeah.
**Cesar Munoz** 32:06 Probably that's what's going on, yeah.
I'll have a loop.
**Hanson** 32:12 But we should separately think about bumping this anyway. I remember us talking about it, we're almost like, yeah, let's just do it, let's just do it, but…
To 23, definitely. Like, if play doesn't support it, I think that's very, very, very compelling.
**Jason Plumb** 32:27 But it doesn't pick this, I mean, that's in keeping with our versioning strategy, I think, but it doesn't fix this problem.
**Hanson** 32:34 No, no, these are now… I'm separating these, like, we should just fix the completable future, kick this down the can, kick this can down the road, and then deal with the version upgrades more incrementally. Hell, we could do it, bump it to 23, wait a couple months, bump it to 24, wait a couple months, and then bump it to 26, wait a couple months.
**Jason Plumb** 32:53 I hadn't even noticed that this issue was filed in gummy bears. It was not filed in… I thought… thought this was in our repo. No, it's… okay, now I'm… now I'm understanding some things that I didn't realize before. Okay.
That's cool.
**Cesar Munoz** 33:08 Cool, but I think we got some… Great insights.
**Jason Plumb** 33:12 I think so.
Yeah, it's a little surprise… I mean, maybe it's not super surprising, but it's nice that no one else has brought this up, right? It means that other people haven't just plugged it in on an old phone and been like, oh, it doesn't work at all.
**Cesar Munoz** 33:28 Yeah.
**Hanson** 33:30 there's a very… there's a… there's a non-zero chance that apps that are using this project doesn't… don't actually support 21. Right. It's… it's like, without actual numbers saying, hey, there are… there are users using it, or rather, apps that are using this SDK that's using it.
Now, they could always use the older version, is the thing, so…
**Jason Plumb** 33:52 Another question on this, Cesar, does this show up as a runtime problem?
**Cesar Munoz** 33:57 Yes.
**Jason Plumb** 33:58 Okay.
**Cesar Munoz** 34:00 Yeah, during compiling time, you… everything's great.
**Jason Plumb** 34:04 That's what I…
**Cesar Munoz** 34:04 when you're running an Android 21 device.
**Hanson** 34:10 It's like…
**Cesar Munoz** 34:10 which is.
**Hanson** 34:11 less…
**Cesar Munoz** 34:11 Animals never supposed to do, to scream at you at compile time, but…
**Jason Plumb** 34:16 Exactly. It didn't.
Okay.
Are we ready to move on?
**Cesar Munoz** 34:21 Yep.
**Jason Plumb** 34:22 No, more, more fun, Cesar. You're bringing all the good stuff this morning. Sorry you're feeling sick, too.
**Cesar Munoz** 34:30 Yeah… Well, it's just that API dump is broken, I created this issue here.
This is a project that has been… this repo where I created the issue.
it seems like it's, maintenance mode only. I think it's,
it's not gonna get any new stuff, because it's deprecated, but still, I didn't know where else I could create this issue.
But yeah.
**Jason Plumb** 34:58 Oh yeah, up here, so…
**Cesar Munoz** 35:01 So, essentially, so what happened? Okay, so to summarize the issue is that…
the, plugin that creates the API DOM task.
**Jason Plumb** 35:12 Checks for the…
**Cesar Munoz** 35:14 existence of the Kotlin plugin in a project, so that it can hook its, you know, API down task.
The problem is that
The Kotlin plugin is something that we no longer have to add, starting with Android AGP version 9.
Actually, the version 9 of AGP
asks you to not add Kotling separately. So, what happens is that
Since we are not adding it separately, this plugin can't find it, so it doesn't know that
it's a Kotlin project, so it doesn't add any task. So that's what's going on.
**Jason Plumb** 35:51 Okay. Okay.
We merged AGP9, didn't we?
**Cesar Munoz** 35:57 Yeah.
I figured this out yesterday when I was checking… changing some APIs, and I ran API dump, and I got an error saying that the task is not found.
**Jason Plumb** 36:10 Which means that we could be breaking… we could be introducing breaking changes and not getting… getting them caught.
**Cesar Munoz** 36:18 Right, yes.
**Jason Plumb** 36:19 Oh…
**Hanson** 36:21 S-so… Jamie, you can talk more about this.
**Jamie Lynch** 36:25 Yeah, we noticed this on the embrace repo a few days ago as well, sweet.
to… have a pretty hacky workaround to basically reinstate those tasks. I've linked it on the meeting notes.
**Jason Plumb** 36:43 Okay, thank you.
**Jamie Lynch** 36:46 It's basically just trying to… Set up the task again, and…
Point the right inputs at it.
**Hanson** 36:56 I believe when you were looking at this, for the Embrace repo, it was working for, OpenTelemetry Kotlin. Or no, was it working for OpenTelemetry
Kotlin, but not Android.
**Jamie Lynch** 37:07 Yeah, that was another weird aspect of it. I think it was related to…
which Kotlin plugin you were applying, because OpenTelemetry Kotlin applies the Kotlin multiplatform plugin, but it works slightly differently than the Kotlin Android plugin.
So my assumption is that… The multi-platform plugin still applies the… Bye. Mike.
Yeah, provide registration for that validation task.
**Jason Plumb** 37:41 So, would you, would Embrace consider donating this?
To Android?
**Jamie Lynch** 37:48 Yeah, we can basically be alphabet.
**Jason Plumb** 37:50 That'd be awesome.
**Hanson** 37:52 Yeah, thank you.
I think we just re-implement it, right?
**Jamie Lynch** 37:57 Yeah, yeah, just, just…
**Hanson** 37:58 themselves, yeah.
**Jason Plumb** 37:59 Copy-pastahead over, I think that would be great. Yeah.
Awesome.
Oops.
Cool.
**Hanson** 38:18 I'm subscribed to the underlying issue, so if they actually provide a fix in the later version, then I should know, and I can remove the two.
**Jason Plumb** 38:28 This one.
**Hanson** 38:30 No, there's an underlying, issue, for, for Kotlin, I think.
**Jason Plumb** 38:39 Yeah, and this Jeff Brains one?
**Hanson** 38:40 Yeah, yeah.
**Jason Plumb** 38:42 Yeah, this one.
Yep.
**Hanson** 38:45 God.
**Jason Plumb** 38:46 Boop!
Oh, I need to be logged in.
**Hanson** 38:50 I got a YourTrack account just so I could go and star that, so…
**Jason Plumb** 38:56 I think… I think I have one, but I'm not sure.
Okay, we are cruising through this hour. I can't believe it's already 40 after. So, there is a POC showing instrumentation module that uses Kotlin API. What is this?
It's a PR.
**Jamie Lynch** 39:16 Yeah, so I just threw this together to kind of demonstrate
to folks who might not be familiar with OpenTelemetry Kotlin, what the API would look like, what the migration buff would look like if we did choose to use it in OpenTelemetry Android.
So… yeah, we don't have to spend, like, ages discussing this, but… Hopefully it'd be interesting if…
Things were able to see, and…
We can maybe even, like, think about starting…
Like, a discussion on what sort of criteria would be for including it.
**Jason Plumb** 39:58 Okay, so that's interesting. So, in the…
**Jamie Lynch** 40:06 So it basically altered the view-click instrumentation.
So, I've… kept using the existing instance of the SDK created by OpenTelemetry Java.
And then, I think there's an extension function to OTOL Kotlin API, which basically wraps that in a Kotlin API.
So you're still using the same thing under the hood, but you get a fluent colon API?
**Jason Plumb** 40:40 Cool, and the only thing this instrumentation produces is events, right? So, and those are based on the logger, so the logger… like, the way I did it before, was it called… I'm just trying to, like… maybe the side-by-side view is better here? How do you switch?
I haven't switched in so long.
**Hanson** 40:57 I always do side-by-side.
**Jason Plumb** 41:00 I never do.
**Hanson** 41:02 I have a gigantic monitor, so I just stretch it out, so…
**Jason Plumb** 41:05 Yeah.
**Hanson** 41:05 That's why… if you use a laptop, that's why you don't do side-by-side. It looks like that.
**Jason Plumb** 41:12 Yeah, I mean, I don't want to go too much smaller, but okay, so previously… so this got factored out, which is fine, and then this got factored out, but…
So, emit the name equals long attribute, long attribute, compared to…
the name kind of being unqualified, and then set attribute, you kind of have to know the types. So, you know, it's a little… yeah, it's a readability, like, trade-off. This reads nicely to me.
We could probably statically import these and improve that, too.
And then, view, emit, view click event, same kind of thing.
Map of… and then previously…
You click, and there was a bunch that would create view attributes were down here before… this thing.
Yeah, so look at how much nicer this reads. This… Compared to this, right?
Yeah, that's really nice.
Yeah, I mean, I guess collectively, we probably want to decide…
When we think it's okay to start relying on that.
Cesar, you… Sorry, Cesar, are you paying any attention to the Kotlin repo at all?
**Cesar Munoz** 42:26 Do you want to? I haven't. I haven't so far.
Bro.
**Jason Plumb** 42:31 oats.
**Cesar Munoz** 42:33 Yeah, I mean, my understanding is, like.
what I wanted to at least wait for is for…
the… all of the signals to be available, I don't know if that's the case already.
But if it is, then… then…
you know, I don't see why we shouldn't start doing the migration, like, this year.
**Hanson** 43:00 So, we still need to implement the API, for metrics.
And when we do that, we can map it over to use the compat version, so still using the SDK… Java SDK. So the metrics right now, isn't there, so I don't think we could migrate the whole thing right now, simply because of the lack of the metrics API.
But, once the API is stable and we're in the process of doing that,
we could start planning, create, like, a milestone in the Opatel Android project, and basically say, these are the things that are required to actually fully move these things over. So, you know, using the…
dependency on Kotlin, and using the compat implementation.
And then switching all the things over, you know, that will all have to be done.
**Cesar Munoz** 43:58 Yeah, sounds good. Is there gonna be, like, a Kotlin… Contrib repo for… extra stuff.
I'm asking because… You know, I'm also thinking about the dependencies that we get from Country.
for Otelandry.
if we still… I mean, of course we can keep them, Even though we… Swap the base.
I think we should keep… should be able to keep him, probably.
Maybe, if we can keep them, even though we swapped Autel Java by OTL Kotlin, you know, we will still be…
tied to the constraints of, you know, the Java stuff that we discussed earlier this meeting, so…
Is there gonna be, like, a disbuffering Kotlin version, or things like that?
And if it is, it's gonna be in the same auto Kotlin repo, or is it… there's gonna be, like, a constrip repo?
**Jason Plumb** 45:01 Go ahead, Jamie.
**Jamie Lynch** 45:04 Yeah, I think…
Ultimately, it'd be good to have a contrary repo, as that seems to be a big convention for…
how stuff works, like, you have, like, the core…
platform, I guess, and then everything builds around it.
Yo.
would say that I think anything that is built using OpenTelebrity Java's API should be compatible if you're running
Like, for compatibility mode.
So I don't see a reason why…
It shouldn't be possible to use.
like, stuff in Java Contrib, unless it's, like, hacking into the internals.
**Jason Plumb** 45:48 But there… I just wanted to pull up this, like, some of these issues, because there is… I mean, you front-loaded a bunch of issue work around the… what's equivalent to disk buffering, I believe, right? So it sounds like… or the intent I gathered from these was that there's a goal to sort of reproduce that same behavior in native colon.
And… Yeah.
We don't… it'd be nice… there's a few of these, it'd be nice to have a… we should create a label for this.
For all the stuff that's, like, kind of persistence-related.
It'd just be cool to, like, have those grouped, but, yeah, that's in progress.
**Hanson** 46:22 We have milestone… I think we were using milestones, for this. So, this is, I think, a mobile ecosystem improvements, milestone, which includes the,
**Jason Plumb** 46:33 Okay.
**Hanson** 46:33 Yeah, the persistence and all that stuff. Like, I think we consider this as being a core function of a mobile-first, or at least user-facing app-first SDK implementation, so this is going to be built into the SDK as an option, to be used, so…
**Jason Plumb** 46:54 What about those Kotlin server-side users, then?
**Hanson** 46:57 They can disable this and not use it.
**Jason Plumb** 46:59 I'm being facetious.
**Hanson** 47:01 No, I mean, there are, I mean, I would love somebody who's using Kotlin on the server side to build services, to…
**Jason Plumb** 47:08 When I was at New Relic, we did.
Yeah.
**Hanson** 47:11 It works just fine.
**Jason Plumb** 47:13 It was great, yeah. Anyway,
Can you show me in this, Jamie, where the Java SDK gets stitched in?
**Jamie Lynch** 47:23 Yeah, I think it's in VueClick Instrumentation, okay.
Yeah, just that line, line 19.
**Jason Plumb** 47:30 Okay.
**Jamie Lynch** 47:33 So, yeah, another interesting…
I guess, option that's available to us is… this is all, like, an internal implementation detail.
like, it's not exposed to any consumer of OpenTelemetry Android.
**Jason Plumb** 47:48 Right. Right.
Yeah, it's really just, like, kind of a thin API layer API. That's why you coded the API around the existing SDK. So in the future.
when the native Kotlin implementation is there, How would this change?
Like, how do we end up getting the other underlying implementation?
**Hanson** 48:15 So, so I, I, this is, like, months ago. I basically ported the entire thing over, OpenTelemetry. So basically, we,
So this is one way of using it, which is basically using extension function to convert an existing Java OpenTelemetry instance to Kotlin using the wrapper. A more comprehensive way of doing this is basically when you initialize the SDK, you use the Kotlin interface to initialize it, so what you get is a Kotlin OpenTelemetry thing, and you pass that down.
And then that could be converted into, a Java version, so that the ones that are using Java API can use it, and vice versa. So this is, like.
this is the piecemeal way of getting in, where the instantiation, the SDK is still Java API, but the instrumentation could be Kotlin. And we also support the other way around, which is the instrumentation is in Java API, but the SDK is initialized via a Kotlin interface.
still using the Java SDK in the core, so…
**Jason Plumb** 49:17 Got it. So this is… I mean, it's whatever this, OpenTelemetry instance is backed by, I guess, right?
Got it.
**Hanson** 49:28 We could pass this bill.
**Jason Plumb** 49:28 So, sorry, this… the interface returned from the OpenTelemetry method here, getOpentelemetry, is going to be the interface of… the interface from Java, but then we have this extension method, which is, like, swizzling it over to the Kotlin version of that same API.
**Jamie Lynch** 49:47 Yeah, that's the current state, and, well, I guess we wanted to change what was on the installation context.
That would be a baking change.
**Jason Plumb** 49:57 Yeah, but that would also be a, like, we would have to change the OTRB…
Which is, I mean, we're gonna have to at some point anyway, that's a…
That's a big change, but, like, you know…
**Hanson** 50:09 This was the 2.0 change I was talking to you about last November.
**Jason Plumb** 50:12 But the OpenTelemetry ROM is the thing that has… that's also an interface? Yeah, the SDK, that's the thing.
would need to change. Yeah, okay, cool.
**Hanson** 50:26 there's, like, a handful of different ways where we could insert Kotlin into this, so it's just a matter of how we want to do this.
**Jason Plumb** 50:34 Yeah.
Yeah, okay.
**Hanson** 50:37 And we've done perf tests and benchmarking. The wrappers make
No difference, in terms of, like, memory and, and, and…
time and things like that. It's very thin. In fact, it improves, you know, improves SDK startup because it does a lot of deferral of class loading, so it doesn't, like, upfront load everything, which is what it currently does. So…
**Jason Plumb** 51:02 Okay.
So, I think it's worth spending another couple of minutes, like, kind of discussing… like, I don't think we have…
in my head, at least, I don't have a clear answer on this question. Like.
if we get approvals on this PR, wherever it went, and, you know, are we okay to merge this tomorrow?
I'm, maybe irrationally nervous about doing that, so I'm curious where other people are landing. I know that,
I know that the Embrace folks are aggressive on this.
No.
**Jamie Lynch** 51:35 I definitely don't want this merged tomorrow, I just wanted to basically kickstart a discussion. I think, yeah, when we get the API a bit more stable, and when we've…
discussed.
Like, what the trade-offs would be, and how we'd actually introduce this into home celebratory Androids.
Yeah, that's when I'd be happy.
**Hanson** 51:57 Yeah, I, I would've, I was…
**Jason Plumb** 51:59 I click this button just to send a signal.
**Jamie Lynch** 52:01 Just…
**Jason Plumb** 52:02 Yeah, thank you.
**Hanson** 52:05 Yeah, I assume this is just Jane putting something up to demonstrate what can be done. This is not the preferred way, I think. I think, if anything, we want to, you know, have an additional thing passed down, in the context that exposes the Java, sorry, the Kotlin, so, API, so that everybody gets it from the context, and then they can sort.
**Jason Plumb** 52:29 herb.
But the upside of this is that it gives you a nice piecemeal way of doing this, right? You don't have to boil the ocean. You can go and pick these apart, and then once they've all been migrated, you can then start bouncing in additional context pieces and start swapping stuff over.
**Hanson** 52:45 Well, the context piece, we only have to pass one thing, which is, like, open thumb to Kotlin. And then everybody gets it, so everybody won't have to do the two Kotlin API thing. They'll just switch the API they use right away, so… Right, right.
**Jason Plumb** 53:03 Right, but one PR that changes one instrumentation is different than one PR that changes every instrumentation.
That's a big order.
**Hanson** 53:10 it won't change it, because it's not… unless you change the implementation, no one's actually using the Kotlin one. So it's… the Java one will be in the context, and there'll be, like, a separate one that is basically, you know, causes Java 1 to…
Great.
**Jason Plumb** 53:24 Okay.
**Hanson** 53:24 Sugar, it's just sugar, so yeah, maybe it doesn't matter.
**Jason Plumb** 53:29 Okay, cool.
Alright, so it sounds like, you know, we're drafting for now, we're looking at ideas, we're sketching it out. I like this approach a lot.
**Hanson** 53:40 It is looking really good. Oh. Yeah.
**Jason Plumb** 53:53 Okay.
Hansen, no update at all.
**Hanson** 53:57 I, yeah, I checked yesterday with, with, with, with Severin, and no updates from them. I looked at where, it's supposed to be in the artifact, and it… I put it where they said to put it, to build it, and it ended up in the class's, jar file, in the meta-in, blah blah blah.
I don't know where… if that's the correct one. I tried Googling, and no one actually… well, I can't find a way to actually tell us we're in AAR, I expect it. Just pre-build where it should be, and it's where it should be. So, originally they said 7 days, and then I looked at the other instructions that said 14 days, so…
who knows? Severin is signing a form and pinging back, but, TLDR, no updates.
**Jason Plumb** 54:47 Okay.
We'll try again in a week, right? Yep. Until we can see something.
Cool.
Right on, I guess that's the best we can do. I have had a little to-do item on my…
notebook, virtual notebook, whatever, for, like, 3 weeks to put an issue into both Android and Kotlin to at least initiate some discussion about supporting declarative configuration. The initial SDK
the declarative configuration schema for configuring SDKs is now stable in OpenTelemetry, in case you didn't see that. And with that, I think there's going to be an increased interest and usage of
that declarative config. What it allows you to do is to initialize an SDK using,
a YAML document that describes all of the exporters, the samplers, all of the different components that you want, and how they should be configured. It's very lengthy, and very detailed.
And then there are also extension points for distributions and instrumentation agents to provide their config as well.
it's definitely worth looking at, and I could see, sometime in the future, us wanting to be able to support this.
because the OpenTelemetry SDK can be initialized using it today, I think it should be possible, but we in Android don't yet have any support for it, right? Like, you can't pass a YAML file to our agent, or have a YAML file in your build, or anything that helps
configure that. It's all done programmatically instead of declaratively. And the long-term goal is to push more stuff toward declarative config.
Because, especially at large… larger organizations that might be shipping a couple dozen different mobile apps, they are able to use one declarative config that meets most of their needs, right? So they have one file in a repo somewhere, and it's just depended on, or passed around, copied, pasted, and it's really nice. So…
Anyway, this has just been on my brain for a while. It's coming, we have to think about it. I will try and get these issues locked.
**Cesar Munoz** 57:04 Sounds good.
**Jason Plumb** 57:05 Yeah.
**Hanson** 57:07 Embrace does a version of this by parsing a JSON file and creating a class file, at build time, so that, you know, instead of having to, like, read and deserialize or whatever, we just read that class file and maps, so it looks at what features are and generates something, so you can, like, programmatically
Map it, so… something similar probably could be done, to basically get this,
Easily referenceable, in the, in the app, so…
**Jason Plumb** 57:35 Yeah, and I'm sure that you would love to not have a bespoke way of doing that.
Yeah.
Cool. Well, it is a client SIG week for those of you that will be joining.
For the rest of you, I'll see you in the comments.
**Cesar Munoz** 57:54 Thank you. Bye.
**Jason Plumb** 57:55 Right.
