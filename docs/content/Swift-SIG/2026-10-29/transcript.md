SIG: Swift SIG
Date: 2026-10-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Nacho Bonafonte 00:00:30 So, good morning, or good afternoon. I don't know where you're at.
Marius Ciocanel 00:00:35 I'm in… I'm in the UK, I'm in Scotland, it's… yeah, it's 4 o'clock.
Nacho Bonafonte 00:00:40 Perfect.
Yeah.
Marius Ciocanel 00:00:45 I think everyone else is, like, North America's an early one for them.
Yeah.
Nacho Bonafonte 00:00:51 It's… Yeah, it's heavier for us.
Hello? Hi, Vladimi.
Vladimir Kukushkin 00:00:58 Hey, hey folks, I just want to… I unfortunately cannot attend today, I just wanted to let you know that the CLA approval is in progress, but unfortunately done for me, so those PRs, unfortunately, blocked so far. I hope it's gonna… get through next week. It's just several, several people who need to formally,
Nacho Bonafonte 00:01:21 Okay, yeah, I can imagine.
Vladimir Kukushkin 00:01:23 Yeah, yeah, otherwise, yeah.
Nacho Bonafonte 00:01:25 No worries. We can… there is no hurry, so yeah.
Vladimir Kukushkin 00:01:29 Cool, thank you. Yeah, great. See you next week. Yeah. No worries.
Marius Ciocanel 00:01:33 Take care.
So I guess we can give people some time.
To…
Nacho Bonafonte 00:01:43 Yeah, for me, I… I should be working on my… On my job.
It's just still my job's time, but yeah, I started earlier today, also, my job, so, yeah.
We got some time.
Marius Ciocanel 00:02:01 We can… yeah, so I guess we can wait for other people, but just wanted to say, you know, that automation bit I did for, kind of, you know, if someone asks, oh, can I make a PR, can I do this and that, and…
Nacho Bonafonte 00:02:18 Yeah, that's right.
Marius Ciocanel 00:02:20 I mean, it's really up to you if you want to have it or not.
Nacho Bonafonte 00:02:25 Yeah, he's not… That's… that's to that, that, yeah, they get a, a quick answer.
Yeah, he doesn't know.
Marius Ciocanel 00:02:34 Which is, like, I mean, I'm happy to close it, because I've addressed it, like I said in the comment, I've addressed it in the… In the documentation itself, Like, in the contributing guide, so I was like, basically… but my thought process was that no one really reads these.
So…
Nacho Bonafonte 00:02:53 Yeah, could be, could be. Yeah, you are true. I think maybe it's something for more people to take opinion.
It's… yeah, that automatic responses are, you know, something… Some days have been too cold, but yeah, probably is better than taking two days or 1 week to answer, probably.
So, yeah, and specifically for that, yeah, let's talk about that later. Is it in the topic?
Marius Ciocanel 00:03:24 No, I'll… yeah, fair enough. I… Yeah, okay, let me put it that way.
Nacho Bonafonte 00:03:29 Put it there so we can, we can admit.
probably we will address it also if we appear in the… when we review the… the PRs.
But yeah.
Marius Ciocanel 00:03:39 Yeah, I mean, it's a draft, so yeah, let's save it for that. Let's save it for that.
I'm not sure if the… I think Ben… and Vishwan are also in the Android SIG.
Okay. And I'm not sure.
Nacho Bonafonte 00:04:10 It's at the same time.
Marius Ciocanel 00:04:12 No, it's earlier, but, like, if it overruns.
Nacho Bonafonte 00:04:15 Okay, yeah.
Marius Ciocanel 00:04:16 There you go.
Nacho Bonafonte 00:04:17 Yeah, I was thinking we were also competing for developers' time.
Marius Ciocanel 00:04:20 No.
Nacho Bonafonte 00:04:21 with Android gear.
Marius Ciocanel 00:04:23 you know.
No, no, it's… it's… I guess… If it overruns, yeah, it overruns into this one.
That's it.
Nacho Bonafonte 00:04:35 Haven't.
Ben Joseph 00:04:38 Hail.
Nacho Bonafonte 00:04:42 Okay, I think probably we can start.
I… Don't know of anyone more who's joining today.
So, yeah.
Let me… Do any other of you want to handle the meeting, or the topics, or something like that?
it's not that I like it, to be honest, but I can't do it if… If not.
Okay.
Marius Ciocanel 00:05:18 Probably easier if you do it, just to…
Nacho Bonafonte 00:05:20 Yeah, could, could be, yes. Sorry for my English, I cannot do it better, just to be honest.
Marius Ciocanel 00:05:25 dollar.
Bye.
Nacho Bonafonte 00:05:31 Okay, yeah, Cocoa Pots Publish, Oh yeah, sorry, we didn't that.
We'll let all of you who didn't do your homework as I didn't.
Awesome.
Okay.
So from Coco Potts Publish, I think that we mentioned last week that it was blocked. Bryce, we are gonna take a look on that.
I don't know.
what?
happened with that, to be honest. I didn't.
Talked to him, and he has not come.
play.
So, yeah, that's it, for that topic from last week.
I think that's the only that… Yeah, interesting information. Yeah, I created a document the other day, yeah, because… there, yeah, I… there were some topics to… or, no, I think Ben did it, right?
Ben Joseph 00:06:47 Yeah, I just…
Nacho Bonafonte 00:06:48 That's already created, yeah.
But yeah, that's great, so we'll put that other public ID during the week.
So yeah, this new topic, Ben, for you.
Ben Joseph 00:07:01 Yeah, I just wanted to, get some feedback. So, I asked this question because, like, we want to advise our customers, like, okay, except, like, the auto library is collecting device ID and transmitting it, so does that require privacy disclosure, what have… have you had any experience? I'm… I'm kind of seeing confusing language on the Apple developer website, so, that's… that's why this question So, device ID, this is strictly not a device ID, right? Like, even… this is identifier for vendor, yeah.
Nacho Bonafonte 00:07:40 Yeah, that's a constant identifier for your vendor. It changed from vendor to vendor, so it's not something that I mean, you can identify the user for your… Oops.
That are with the same, but not for another third party. So I don't know. I don't know if it requires it or not.
So, I would.
Marius Ciocanel 00:08:03 I am not.
Nacho Bonafonte 00:08:04 But…
Marius Ciocanel 00:08:07 So I have… I've seen that and, like, basically asked, quote, to do a bit of research into this, and also run some tests on device. And the identifier, like, the vendor identifier.
changes, so even the same app with the same bundle ID, if you delete and reinstall it, you get a new one on the same device. So it's not… and yeah, it said that it kind of breaks the… I guess the specification that, you know, that this data is expected to have, and instead of that, we should be using the,
Ben Joseph 00:08:50 That's okay.
Marius Ciocanel 00:08:51 installation ID, yeah, because it's more of an installation ID rather than a device identifier.
And yeah, so I ran it on… on a device several times, deleting it. Well, Claude ran it on my device, and it… Every time you delete it and reinstall, you get a new identifier.
Nacho Bonafonte 00:09:12 Even if you reinstall from test flight.
or Xcode, or the App Store as a developer, it's…
Marius Ciocanel 00:09:19 If you delete, you change. I remember we… in the SDK I worked on before, like, we had to kind of work around that for a bit, and we put something in the keychain that would… kind of survive. I mean, it was a workaround, not really… Not sure how Appa, like, you know,
Nacho Bonafonte 00:09:40 Yeah, I mean, I think the App Store, if you update with the App Store, it doesn't change, but yeah, it's not… yeah, also saving a local value somewhere, is the only way, but if they delete the app, they get a new one, and you cannot do… and you cannot recover that.
But never, even if.
Marius Ciocanel 00:09:58 Beno.
Nacho Bonafonte 00:09:59 If you're keeping the kitchen, also.
So, yeah.
Marius Ciocanel 00:10:02 Cool.
What does Android do in this case, Ben, do you know?
Ben Joseph 00:10:07 Yeah, so Android… so device ID, I think, as per… Yeah, specifically for Swift, I think, like, on the hotel website, like, there's a, you know, this device ID should use Identify for a vendor, but, like.
The, the common language, outside of that is device ID is a hardware device identifier, like, you know, IMEI, or something that is very specific to the hardware, and that cannot change.
So that's how Android treats device ID, so it does not automatically collect and send it. For this particular use case, there is a random UUID generated by By the SDK, in the case of Android Auto, and that's what it sends us, app.installation.id.
so, I… I… If this changes per installation, I think app… app.install.id is a more fitting
Marius Ciocanel 00:11:06 Damn.
Ben Joseph 00:11:07 name, but I… I also did not test this. My understanding was that, like, if you have… if you install the same app with the same signing key and the bundle identifier, I thought you would get it… get the same thing back, but… No. Okay.
Maybe in that case, it's worth renaming, yeah.
Device ID is slightly misleading. I don't know if you guys…
Nacho Bonafonte 00:11:31 But yeah, that's true, but that's the name that Apple uses for it.
So if you are a Swift developer, it's called device ID for Apple platforms, even when it's not a device ID.
So… Yeah, maybe… duplicating it.
could make sense, if there are other uses, maybe in Android with installation ID, so we could report both.
But I don't think removing device ID as a name, w-would… Would be good for, for maybe, yeah, iOS, or Apple, Let's say, naming.
Sometimes you also have to, you know, be able to associate the names with the platform itself, but yeah.
Ben Joseph 00:12:24 Cool. Like, so the workaround we do is, like, we map device ID to app install ID on the receiver end, so that the backend can, you know, on both platforms, look at the app installation ID.
So if everybody feels that way, like, I can definitely make a change. It's not a deal-breaker. Yeah, and I… maybe not a good idea to break something that already exists. Device idea, rename it.
But if people feel strongly, we can add another app install ID.
Marius Ciocanel 00:13:00 I think it's… personally, I think it's more suitable to… to have on… like, installation ID. I think that's also part of the spec. I read some comment… I'm trying to find where I read the specifics about the differences, because I saw it in a documentation somewhere, I can't find it anymore, I've got too many things open.
But if I do find it, I'll share it in the chat here.
Nacho Bonafonte 00:13:25 Yeah, I mean, if you think it's useful, I will duplicate it, so reporting both.
But I… I think keeping the platform name, in this case, and something that has been working probably should be kept.
But duplicating, I'm okay with that. So yeah, as, as you, as you prefer. I have no strong opinions in each side.
Except removing it. Yeah, that's… I think that… Should be… wouldn't be good.
Billy Billy 00:13:58 Just out of curiosity, which privacy disclosure are you talking about, Ben?
Ben Joseph 00:14:05 Sorry, one second, I'll come back to that. So, here, device ID, right? Like.
it all says its values should be identical for all apps on a device, so this is not… True for identify for vendor.
So that's… that's where it's slightly confusing.
But somewhere else, I, I also, remember seeing, like, on, on, iOS devices, this should be the identifiable vendor. I, I don't remember where it is.
Marius Ciocanel 00:14:37 Yeah, so in the yellow, the warning.
Ben Joseph 00:14:39 Oh, yeah, yeah.
Marius Ciocanel 00:14:40 Mentions exactly this.
that…
Nacho Bonafonte 00:14:57 Yeah, maybe we should add also something there in that, the official documentation.
Ow.
Because that's the… That… so, adding that… maybe iOS has also a different use for that.
but yeah, you don't have…
Marius Ciocanel 00:15:17 That if it's wrong.
Nacho Bonafonte 00:15:19 thereby Sadie, on, on, on March.
Marius Ciocanel 00:15:20 This is…
Nacho Bonafonte 00:15:21 Alright.
Marius Ciocanel 00:15:22 It's down a bit… yeah, it sees… it says, see app installation ID for more privacy-preserving alternative.
And it also says, should really be using the device ID.
Only in certain cases.
Nacho Bonafonte 00:15:49 Yeah, I… That, yeah, that… Yeah, I don't know.
I think this is very risky.
What they say.
it will result in rejection from both Google Play and App Store.
you don't have a way to have a number on iOS, anyway.
Marius Ciocanel 00:16:22 You know… Not something that persists between installations anyway.
Nacho Bonafonte 00:16:30 Yeah, thinking about Manage, Devices?
Maybe you have an MDM identifier somehow?
Marius Ciocanel 00:16:40 But if…
Nacho Bonafonte 00:16:41 But that should be only for supervised devices, or something like that, which is…
Marius Ciocanel 00:16:48 Also, if that is true, that would be populated by someone that isn't this SDK, so it wouldn't be our… the responsibility of us to… To put that, privacy…
Nacho Bonafonte 00:17:03 Yeah, if you're in a supervised device, Thinking if you can…
Ben Joseph 00:17:09 No, I mean, the Autel SDK will not have access to that information anyway. I mean, if you're… if you are within the supervised app, then you have Probably have the privilege to call that, but… If it's just… like, an agent managing… like, if it's… you are an app on a supervised device, you will not have access. Only if you are within the supervised app.
I believe you will have access to that API, right?
So, the MDM Spawn app, MDM Agent app.
Nacho Bonafonte 00:17:46 You mean an MDM installed app?
Ben Joseph 00:17:49 installed app will not have privileged access to call supervised APIs, right? Like.
Nacho Bonafonte 00:17:55 Nope.
I think not.
Yeah. I think even an app installed from the MDM has that knowledge.
Ben Joseph 00:18:01 No. No.
Nacho Bonafonte 00:18:02 So probably… so that's… I don't know. I think we cannot get…
Ben Joseph 00:18:08 Yeah, and maybe…
Nacho Bonafonte 00:18:09 Device identifier, anyway.
Ben Joseph 00:18:12 Yeah. I mean, that's not even, required, I think. Like, that is, like, I mean, that's PIA, and, like, we definitely don't want to deal with that. Like, it's better for us if we can, like, move away from a hardware or, like, fixed ID. Like, an FMRL ID is the most preferred, like.
So that's what, like, the app installation ID is for. You… you… when you first launch the application, create a random UID and persist it. If the app is uninstalled, it's lost, and that's the best case scenario.
So, when you install it new, it's a new installation altogether. But, that particular instance of the application, you can identify using the CUID, And that's… that's all we need.
Marius Ciocanel 00:18:57 But… I mean, you are… what you're describing now is the behavior of the vendor identifier.
Ben Joseph 00:19:05 Yes, that, that is the behavior, but, like.
The only confusing bit is, like, device ID, Is there, device identifier, that… that should remain the same, like…
Marius Ciocanel 00:19:27 So I think…
Ben Joseph 00:19:28 Yeah. Identifier vendor is the correct, correct, identifier, but, like, what we call it, or how we,
Marius Ciocanel 00:19:35 That should be installation ID. It should be installation ID rather than device ID.
You know, the vendor identifier should map to the… the installation ID. Is that what you're saying?
Ben Joseph 00:19:46 Yes, that is what I was suggesting. I'm not… particular on it. As I mentioned, like, we do that mapping on our backend because, Yeah, that's… Easier for management, and, like, it fits into the hotel semantics.
Nacho Bonafonte 00:20:03 Yeah. Yeah, I agree, that it doesn't follow the semantics, but… Yeah, it's sad.
breaking change, I think?
It's a value that… it cannot be cut. I mean, you cannot get that value.
I thought that you cannot get a fixed value for that.
never on iOS, so I think… that… Taking that as granted.
You must know that this value, even if it exists, cannot be… a fixed value. You cannot do that with… Okay. Maybe you can do that with a Mac?
If you save something on the hardest, and you have some kind of privilege, and you are not sandboxed, and you…
Ben Joseph 00:20:54 And those are all…
Nacho Bonafonte 00:20:55 you report your Wi-Fi… MAC address, you know.
Ben Joseph 00:21:01 That also requires, like, privileges, right? Like, location.
Nacho Bonafonte 00:21:04 Yeah, that's right.
Ben Joseph 00:21:05 Even if you want to get MAC ID.
Nacho Bonafonte 00:21:08 So… Yeah, I… yeah, I will… I will… as I said before, I think we should keep pit, at least, on device ID, and maybe If you think it's interesting, also add it as the same value as another… in another field.
On the attributes, so it can be read.
as, as what it is. But removing it.
At least for now, automatically, I wouldn't do that.
Ben Joseph 00:21:36 Yeah.
I agree.
Marius Ciocanel 00:21:42 I guess your other question, Ben, was do we need a… doing… needs a… privacy,
Ben Joseph 00:21:50 Yeah.
Yeah, so Billy was asking. So, I don't know the exact process, like, when you submit the act.
After review, you also disclose what kind of tracking or, identifiers you use, like, a set of privileged APIs, so is this something that, like, or, like, Apple can identify you are already, using the identifier vendor API, right? So, do you need to explain how you use that data returned from that API, like, oh, is it… this is for telemetry, or tracking, or… Are… app developers expected to provide an explanation for usage of this API.
Billy Billy 00:22:40 Just by reading about it, there's, like, the privacy and nutrition labels, right? I've never done it myself, so I'm not gonna speak on it, but, Has anyone else, like, you know, Gone through that before?
I see that there's just, like, very clear instructions about, like.
You know, the various levels of data that they're collecting, regardless of, like, what you intend to do with them.
Marius Ciocanel 00:23:06 So, I've pasted an example of, like, Sentry, what they do, just because I'm still reading up on, what you need to provide, because, yeah, the… I didn't have to provide that for… for the SDK I used to work on.
I'm assuming these… you provide reasons for why you use it. I don't know what that CA92.1 means. I'm assuming they're… Taken from somewhere.
Nacho Bonafonte 00:23:39 Yeah, you, you must… you must explain to Apple what are you using specifically. It's… value for… yeah, that's something you must do on the… On the, on your app when you upload it.
So it must… this, this, privacy, must be with Europe when they are going to approve that.
Ben Joseph 00:24:06 Okay.
Marius Ciocanel 00:24:06 Thank you.
Nacho Bonafonte 00:24:07 Yeah, it's sad.
You know, Apple bureaucracy.
Which, I mean, yeah, it's your tool.
To try to track those who are not using it properly.
Marius Ciocanel 00:24:24 I guess the way I interpret your question, Ben, is that if… I guess, if we don't… I don't think we do need it, Not just for the device ID.
Oh… Unless… I think, like, there was, again, a documentation somewhere. Unless you combine it with other things to make… but we don't… I mean, we. Like, this SDK doesn't do that.
However, whoever integrates the SDK might, and in that case, their app should… Include that, because… You know, they're basically combining data to make.
Ben Joseph 00:25:13 Yeah. Easy.
Marius Ciocanel 00:25:14 User tracking.
Ben Joseph 00:25:15 Salt. Yeah.
Yeah, I think that's all. Blake.
Yeah, I kind of get the idea.
I think it's, just declaration. Yeah, thank you, thank you for answering that.
Nacho Bonafonte 00:25:36 Okay, so the… the following topic is… Yeah, there was an issue open about using Optana optional integration with Pipette Strait.
Yeah, that's the… I don't know if you have seen it. We already talked about this in the past.
on this SIG meeting when it appeared this version of Swift.
And we came to the conclusion that Wouldn't that work?
But… It looks like we failed on our conclusions then.
And this user is saying that it can be done. So basically, it's… adding traits… To each of the packages, and he says that if you're… dependency… is not part of the trades yet that you are using, it's gonna… it's not gonna download its… dependencies.
Itself.
That, that's, that's what we… We'll have, like, to do when we move the core libraries out of the… Of the main repository, and we bring it back.
We moved there because… How many dependencies it was downloading?
Which was, Yeah, which, probably you are seeing, right? Especially if you're installing a CI, it takes, Lots of time downloading the third-party dependencies for libraries that you are maybe not using.
So… Here, the user says that it can be done like this.
Right? Like, cutting the… the traits… For each of the functionality, and… And when you import it, just defining what Threads you want to use.
And that we bring them together. I don't know if you… any of you have… experience with this treasure. I remember with… Talked about this, someone took a look and… Came to the conclusion that it could not be done.
But… it… This user says exactly the opposite, and even offers to create a pull request, which will be great.
So, what do you think about this… Would you like using the library like this?
Using here the trace that you need, and avoid That's a usage by basically for our users. It's a way, you know, what you really use, and try to really use from from the SPM while libraries are being downloaded. We have talked about this many times, even with the Apple engineers in the past.
And they… didn't offer this as a solution, so for me, it surprised me that it… works.
Marius Ciocanel 00:28:48 I mean, from a conceptual level, it sounds like… how Cocopus dealt with, like, subspecs, so you had a core, and then, you know, it had… you'd add multiple things, depending on what you needed. And it kind of… I guess from a… from a theoretical perspective, it makes sense.
Nacho Bonafonte 00:29:11 Yeah, yeah, I mean, it has been a hole in SPM for a long time, that it's a pain in the ass, for big projects, or…
Marius Ciocanel 00:29:20 But how would…
Nacho Bonafonte 00:29:20 Many targets like us?
Marius Ciocanel 00:29:22 So, how would that work in practice, though? Would the code need to have, you know, like, if this trait is installed.
then use this, you know, like, include this code in the build. I'm not really sure.
Nacho Bonafonte 00:29:35 No, it… if… It defines trades, on your package, like this.
And it says which targets?
Depends on which, trait.
So it doesn't build those targets if you have not… when you use the package.
For example, for this example, it will only include Jagger trait?
Marius Ciocanel 00:30:03 Okay.
Nacho Bonafonte 00:30:04 So, only… those… targets that have Jager in the name will be included, and only the dependencies… of the targets that include the Jagger trait will be downloaded. That's what he says.
Which…
Marius Ciocanel 00:30:22 Right. Okay.
Nacho Bonafonte 00:30:22 what we would like. So I told him about talking, about talking this in the SIG meeting.
Because it sends a bit the way it's used.
And we also must test that it works, as he says, right? But if it works, I think it's… it's really nice for… because, for example.
Yeah, this TripSuite library, it's a very old library that I bought myself because I had to fix that.
And it's, hanging from a… did have a repository of a company that's not anymore, that I worked several years ago.
So it's there, and we are still using that, because there is no way for the original library to support what we needed. And we have the same for OpenTracing, for example. There is also a For the OpenTracing SIM target, we are using another fork of OpenTracing Swift that I did myself years ago, because we needed something that the maintainer of that library never landed on the… official library, because it was updated with OpenTelemetry, so… I think it's… if it works, it's good, but I don't know if… or if you… Think the opposite, any of you?
Or we can ask him to just, create a PR, so we can really evaluate.
Basically, the thing is, Do you think it's worth adding this?
Or… or it's better if we really avoid downloading other dependencies that we don't need?
It will probably also allow us to support different versions, for example, for Linux?
So, you can have different… Versions of dependencies, depending on your usage?
Or… Maybe for,
Marius Ciocanel 00:32:14 Vladimir, I think, mentioned something about using traits to support Linux, so… maybe.
Nacho Bonafonte 00:32:22 Yeah, could be… maybe we can ask… ping? Can we ping him here, maybe?
So, he's probably the most knowledge.
Person about this, in this meeting.
Ben Joseph 00:32:44 And we can also ask them to open a request. I think there's no harm in that.
Nacho Bonafonte 00:32:50 He said that he is happy to open a pull request himself, so…
Ben Joseph 00:32:54 Yeah.
Marius Ciocanel 00:32:55 Just even a draft one is fine.
Nacho Bonafonte 00:33:09 It looks like I… Yeah, maybe we can ping Vladimir then in the PR beta?
Or should we ping him here? What do you think?
Ben Joseph 00:33:47 maybe CC Vladimir.
Marius Ciocanel 00:33:49 Yeah. Yeah.
Nacho Bonafonte 00:34:01 Great.
Marius Ciocanel 00:34:02 I think it was with a K.
Nacho Bonafonte 00:34:03 Nope,
Marius Ciocanel 00:34:06 K something, something.
Nacho Bonafonte 00:34:08 Oh, oh, yeah, the key, yeah, he's…
Marius Ciocanel 00:34:18 Wait. Okay.
Nacho Bonafonte 00:34:19 Yeah, I will, Kukushko SIG… Yeah.
It's great.
Oof.
Okay, sorry.
I don't know, it is his surname, I think.
But… which one?
Oh, he created some…
Marius Ciocanel 00:34:51 Issues in, yeah.
Ben Joseph 00:34:52 I think it's K… KUKU…
Nacho Bonafonte 00:34:56 Okay.
Ben Joseph 00:34:56 Okay.
Nacho Bonafonte 00:34:57 Yeah, thanks.
Ben Joseph 00:35:02 KAU.
SH.
Is it not,
Nacho Bonafonte 00:35:08 But he's not appearing here.
Ben Joseph 00:35:11 Let me, post it in the chat.
Nacho Bonafonte 00:35:15 Cool.
Marius Ciocanel 00:35:17 Maybe I should just right-click and copy.
You can say, you are talking about this.
Nacho Bonafonte 00:35:42 I don't know if he will see this.
Marius Ciocanel 00:35:45 Okay, yeah.
Nacho Bonafonte 00:35:47 And I… Yeah.
Marius Ciocanel 00:35:49 schema.
Nacho Bonafonte 00:35:53 Yeah, great. Yeah, this is… Yeah, so we can get that also, if… so he can also evaluate if that's possible and that works as expected. That… that will be great, to be honest.
Okay, more topics.
Yeah.
This is something I just came with.
Our README is a bit updated, out… outdated, sorry.
Because I, I, I, I, I see we are still maintaining, Swift 6, Aspercion… And we are missing some, some of our instrumentation.
Billy Billy 00:36:43 Oh, yeah, as far as to…
Nacho Bonafonte 00:36:46 So, yes, bringing this here, so if anyone wants to update it, on… on… Yeah.
Oh, these are… these are updated, but we are… we still have some other… Some other things that are missing, like… Yeah, it's to maintain… I think we… all the… Swift tracing libraries, and some of them, just to have it clear. And also, the version of Swift, I think it mentions 5, and we are clearly on SWIFT 6.2, and things like that, so if… Anyone?
It wants to take this as a task, it would be great just updating.
the content there. It should be quite… Did it, some review.
Ben Joseph 00:37:37 Should we create an issue for a good first issue or something like that?
Nacho Bonafonte 00:37:41 Yeah, okay, yeah, that, that, that's, yeah, that's a good idea.
Marius Ciocanel 00:37:48 Also, I could probably take it, since it kind of will take me through the entire codebase, just to… See what the differences are.
You don't have to assign me, I'll have a look at it after that.
Nacho Bonafonte 00:38:01 I can, I can't sign it, but…
Marius Ciocanel 00:38:36 Updated.
Ben Joseph 00:38:38 fixed.
Nacho Bonafonte 00:38:40 Yeah, yeah, I was trained not to use updated, or outdated, updated initially.
Ben Joseph 00:38:44 Yes, yes.
Nacho Bonafonte 00:38:45 My vocabulary is quite limited.
Ben Joseph 00:38:48 No worries.
Nacho Bonafonte 00:38:49 Okay, so, I think that's the other… see, what? Sorry?
Marius Ciocanel 00:38:55 I have a.
Nacho Bonafonte 00:38:55 Do you want me to assisting you?
Marius Ciocanel 00:38:57 It's okay, it's, I'll…
Nacho Bonafonte 00:38:59 Oh, oh, sorry, I, I, I,
Marius Ciocanel 00:39:02 If you want, sure.
CIO.
C-I-O… C.A.
NEL, yeah.
That's very weird.
Nacho Bonafonte 00:39:20 Yeah, I don'.
Marius Ciocanel 00:39:20 Maybe it doesn't do full, it's okay, just leave it, I'll… I'll look at it.
Nacho Bonafonte 00:39:26 I will remove myself.
Marius Ciocanel 00:39:27 But I actually wanted to ask, since we're talking about version numbers, and like, I saw when we were looking into the device ID thing.
there's a version for the OpenTelemetry spec.
What version… what version do we, you know, does…
Nacho Bonafonte 00:39:45 We have video.
Marius Ciocanel 00:39:46 imagery.
Nacho Bonafonte 00:39:47 We are very updated on this, but…
Marius Ciocanel 00:39:50 Is it anywhere? Like, are we… Try keeping track of it anywhere in the repo, or… Should we?
Nacho Bonafonte 00:39:58 Yeah, I, I, yeah, I was… Yeah, I… I will… I will explain it a bit. Yeah, there is a semantic convention repository for OpenTelemetry that where all that is updated.
But the way to create the files from that?
I've changed several times.
For the life of this project.
And from Open Delimited. So… We've had everything working for the… At least two first ways of generating those, automatically.
But now they change to something new that, we are not following. So there's… PEC cannot be automatically updated.
Because we have… We, we, we have not updated that.
For the… in the part, we had that more or less automated, so we had some scripts that ran on Docker, blah blah blah, and it generated the Swift files, that we used for the Spectre. But now has changed, and we need other, other scripts and other things to update, yeah.
So…
Marius Ciocanel 00:41:08 Would doing something… I guess, would working on something like that be useful?
Like, on the automation.
Nacho Bonafonte 00:41:13 really awesome. If you can take a look at that, it will be really awesome, because we are… we are out of… out of date. And now, as everything is now on the same repo, it should be easier.
I think in the past we've had something… I don't know exactly, probably in the screen.
Ben Joseph 00:41:33 I think it's Scripps. Yeah, Scripps, SSM, and the convention.
Nacho Bonafonte 00:41:37 I have this… Where we had a generation, some templates that we used for generating, and yeah, this was done automatically.
In the past. But the way… Yeah, it was using, you know, this is our version we have.
Which is probably 2 years old.
Marius Ciocanel 00:42:00 Well…
Nacho Bonafonte 00:42:00 I don't know.
Marius Ciocanel 00:42:01 If I remember… if I remember correctly, when we were looking, it was something like 1.4… Or something.
For sure.
Nacho Bonafonte 00:42:08 It's weird.
Marius Ciocanel 00:42:09 for it, yeah.
Nacho Bonafonte 00:42:09 Yeah.
Marius Ciocanel 00:42:10 Yeah, okay.
Nacho Bonafonte 00:42:11 I mean, the spec… the real… the big changes on the spec happened at the beginning, right? So now they are usually a small thing that, you know, is nice to have, but… We have not seen that.
Yeah, we had this Docker thing that ran everything, but now they change everything.
And the… the things are generated in another way, so… The templates that we have for generating doesn't work anymore.
So yeah, that… Okay.
Marius Ciocanel 00:42:41 Oh.
Nacho Bonafonte 00:42:42 That's the reason it's not updated. So, if you can update that, it will be…
Marius Ciocanel 00:42:45 Yeah, I mean, if… if… I'll create an issue for this, and okay.
just to, I guess, investigate the automatically keeping up to date with the latest.
Nacho Bonafonte 00:42:59 I mean, automatically, or just having something that… I mean, this was a script you had to run it.
Marius Ciocanel 00:43:05 I'm just fixing this script, basically.
Nacho Bonafonte 00:43:06 generate the files that put in the proper folders and just update, right? We don't need to hover with the latest thing, but an automated way of updating will be great.
That, that, that's, that… it's not an easy task, but, It's really useful, for many people, yeah.
Marius Ciocanel 00:43:32 I'll open a… I take care. Well, an issue for now.
Let's see if I can have a look.
Nacho Bonafonte 00:43:53 Okay, yeah, okay, that… That's the topics we have.
Any other topic you have in mind?
I don't think there are many things here on the issues.
new issues… no, nothing new. This is the… Package streams that we have talked already.
This is the Rhythmia we just created. Regarding pull requests, I… I think we are in a similar situation still with the URL session instrumentation.
Which is… which is very bad.
Thinking if with trades we could do something with this?
So, something like having… ZRPC Swift 1 or Swift 2 versions for… maybe some of the dependencies, that would be awesome. I don't know if we can get that with trades, but… It will solve problems for many people that want different versions of dependencies.
And different versions of the compiler, right? If we need to move to… Something newer, maybe?
just knowing that with a trade, you have a more reduced number of buyers versions, that would be great. And that… if the trades work, that's also a good idea.
Marius Ciocanel 00:45:17 I think that… the issue mentioned that the trades work on Swift 6.2 and higher, which is what our minimum is.
Nacho Bonafonte 00:45:28 Yeah, but the thing with this ZRPC suite, I think it's because it had a minimum version of iOS higher than the default, so… So the thing will be having trades, to support dependencies that have a higher minimum iOS version than the one we support, for example. So, if they need iOS 18, because they are using concurrency framework from Apple, for example.
and we are still supporting iOS 15, maybe we could have different Targets for different persons with traits.
It's a bit of, you know, maybe complex, because we will still have to Build on different versions for testing properly, but yeah, that could… also work.
Regarding the URL sessions ones, I think that we are still in the same position that we were last week, I don't think it has been updated. Yeah, it still has conflicts.
yeah, and Ben already asked for that in that branch, and many others, we have that.
Okay.
Marius Ciocanel 00:46:38 Cool.
I'm curious, what happens if, you know, like, because obviously, like, people are voluntarily contributing PRs, if they don't respond.
Nacho Bonafonte 00:46:50 Yeah, we, we've had Hello, I mean, yeah.
For example, here… in this one.
Marius Ciocanel 00:46:58 someone else, like, brings in, I guess, a PR with similar functionality, could we take that instead, if, you know, we give them an opportunity to?
I'm just… it's more about process and, like, how…
Nacho Bonafonte 00:47:10 Yep.
Marius Ciocanel 00:47:10 Things are decided.
Nacho Bonafonte 00:47:11 It seems that…
Marius Ciocanel 00:47:12 stuck, yeah.
Nacho Bonafonte 00:47:14 Yeah, the… Let's say that the copyright of that code is from the user who wrote it, let's say.
Especially they don't have him sign the… the club.
So they have not donated that code, so that's, kind of a LEGA.
Marius Ciocanel 00:47:33 No, no, I mean, I wasn't saying…
Nacho Bonafonte 00:47:36 Yeah, the thing is, we could recreate these same fixes in this or in a different way. If you ask your LLM just to read it and regenerate in a different way, you have no copyrights there.
Probably.
We asked him… For the changes, because that will give him credit.
We could also… You know, fix the… fix ourselves because he has the AC class sign, so we could try to… fix the conflicts ourselves in these branches if they are public. Maybe they are not and cannot be modified. And if not, the other option is just recreating that and fixing in another branch, and dropping this one.
But yeah, it has been, like, open for a long time. I don't know if it's still around, or just no… Life cycles, recently. He… Updated one of those peers?
And, and I immerse it, like… two weeks ago, I think, if I remember correctly, at three, but no, no, no more. I don't know. So… he gave life signals, like, 2 weeks ago. Maybe he will come back, maybe he's very busy, I don't know. But if any of these things is critical for your work.
Yeah, we, we can, we can address it, in another PR.
totally… Yeah.
Okay, for the rest of the… this, Okay, I don't know what's this.
Marius Ciocanel 00:49:19 Probably first-time contributor.
Nacho Bonafonte 00:49:23 the method of our method. Okay, let's make it run, I have missed… Why did I… I, I was thinking why I didn't review it. I haven't… Checking all the peers, almost every day.
And I have missed this one, I don't know why. Probably because it was very near to the… to the URL session, and I forgot? I don't know, sorry.
But it has been without review.
Okay.
This one about… Yeah, this one, I think, is the one that Vladimir mentioned.
Is that it's failing the ICLA?
And I think it's missing the ECLA…
Marius Ciocanel 00:50:19 No, this… I think this is because there's a blood code, no reply at Anthropic that they need to remove and push.
Nacho Bonafonte 00:50:28 Oh, okay. Oh, the… but even…
Marius Ciocanel 00:50:31 Yeah, even their own, yeah, it's not done.
Nacho Bonafonte 00:50:34 Yeah, so yeah, we need that in order to Naked.
If not, we can… Yeah, recreate it also in the same way.
Another PR, PR… is this one. I think this one, this is the one that… I think… He applied… Yeah. He applied some changes directly from comments from Vladimir, and Vladimir has not signed Dick.
Declat.
Because he's still in the process with Apple. He has joined the meeting in the first minute to say that he's still on this, and we expect to have that. So, yeah, don't apply.
Vladimir comments directly, because, yeah, basically I will say it's… it's bad. But yeah, he… he expects to fix that.
And he even approved, but yeah, we need the ZCC cloud here to merge, but it will merge whenever we have that, probably next week, as Vladim mentioned.
Which is great. This one?
Yeah, this one, this topic.
That…
Marius Ciocanel 00:51:52 Yeah, no.
Nacho Bonafonte 00:51:53 something Marius did, which is an automatic response for those who say.
Can I be assigned to this?
Issue.
okay.
Basically, this is something we should talk, all of us, in this meeting. Do we want… I mean, it's cool.
to have something that automatically says to people, can you assign me? To say, no, create a PR, anyone can do it. We don't need assignment.
Marius Ciocanel 00:52:24 I mean, it's a softer wording than that.
Nacho Bonafonte 00:52:27 Yeah, yeah, that's true, true.
But… The thing is, do we want that? Do we think it's too cold?
I'm not sure. I said it's maybe too cold.
Marius Ciocanel 00:52:41 My thought process was that… We want to tell people that, yes, we welcome contributions.
as they're motivated to contribute? Because if someone asks a question, and then, like, even, like.
they get an answer the next day. Even 5 hours later, you know, like, I moved on, I don't really care about this anymore. Maybe, I don't know, with attention spans, like, it's… my thought was that we just give them the permission, and just kind of encourage them to do it.
without… us having to say anything. It's… it's not… it's not reviewing the PR automatically, and just… it's more about… Kind of, you know, Encouraging people to contribute if they really want to.
Yeah, that… that's the check if, you know… That's the message, really.
It kind of goes with the documentation update I made earlier.
Because I was… I wasn't personally sure, you know, how does it work? Like, you know, if… if I see an issue and I want to take it, someone else asked, do I still go? It's just not… super… Kind of clear, and people don't tend to read the documentation very often, so they will still ask.
Ben Joseph 00:54:11 Should we just add a note to README instead? I'm… like, this is very nice. My hesitance is adding one more piece of code that we need to maintain.
If anything, with respect to the workflow changes, it's one more piece to maintain, instead of, like, a line in the README.
Marius Ciocanel 00:54:32 Yeah, the README, like, from my personal views, and like, I've said it in the comments, like, the README has already been updated, like, the contributing guide, to say, pick up anything.
this was… this was a bit extra. Like, I'm happy to drop it, this is why it's still a draft, and I didn't push it as a… because I wanted to get some feedback.
I'm not… Like, I don't know, like… super tight, or… to this, like, having to go with either.
And…
Ben Joseph 00:55:03 I'm… I'm okay to have it, like, maybe, like, maybe let it run for a while, and, like, once people are used to that, then maybe we can remove it. If there's no harm, we can do it.
I don't have a preference either way, I think.
Nacho Bonafonte 00:55:18 Yeah, to reinforce Marius, I don't know if he has a friend, but, someone asked here, hi, let's work on this, and this was 17 hours ago. I'm asking, could you assign it to me? So, I don't know if it's Marius' friend, or something like that.
Marius Ciocanel 00:55:34 No, no, it's not.
Nacho Bonafonte 00:55:35 Who's…
Marius Ciocanel 00:55:35 When I…
Nacho Bonafonte 00:55:36 something here, because it sounded very… but…
Marius Ciocanel 00:55:40 Can we try it for a week, and then I promise I'll remove it if it does… if, you know, let's see how people respond.
Nacho Bonafonte 00:55:49 Yeah, I, I agree. Would your, you know, would your script itself cut this one?
Marius Ciocanel 00:55:56 Yes, yes.
Nacho Bonafonte 00:55:57 Okay, great. So then… Do it manually this time?
Billy Billy 00:56:04 Could we remove the, detection and just, like, post the general contributing guidelines? I think that makes sense.
Nacho Bonafonte 00:56:09 Let me just handle this.
Billy Billy 00:56:10 tomorrow.
Nacho Bonafonte 00:56:11 this time?
Preview… oh, yeah, that's great.
Thanks. That, that's the manual handling, but, do you want to see the, the… the script there?
Marius Ciocanel 00:56:27 So, I can show you some links, because I tried it on my fork, because obviously, like, it's automation, so, like, I wanted to make sure it works. If you look in the description of the PR, I linked to a few examples of, like, when Like, I tested it on one of my forks, so it… here you go. If you have a look at one of those, like, 4 or 5 or something, like, no, if you scroll up a bit, there's links.
Nacho Bonafonte 00:56:58 Oh, shit.
Marius Ciocanel 00:56:58 So it's… yeah, those. So these are kind of examples of… what it looks like. That's it. Can I work on this? And it only shows you… and it only does it once per kind of issue.
So it doesn't spam you, like, with, like, several ones. It's like, it says it once, you know, someone asks, like, because for a PR, there were two people who asked for this, and then a third person came in with a PR, and like, if I was waiting for an answer, like, I'd be pissed. Like, if someone comes in and swoops and takes the PR I wanted to…
Nacho Bonafonte 00:57:33 Okay, yeah, you have… yeah.
Yeah, you…
Marius Ciocanel 00:57:38 If it doesn't work…
Nacho Bonafonte 00:57:39 I raised my hand, and I'll…
Marius Ciocanel 00:57:41 And I'll remove it myself. It's literally just a workflow.
But it was so funny, because I did not see that comment.
Yeah, you know.
Nacho Bonafonte 00:57:54 Yeah, I just thought of, wow, it's such a great timing for that comment to come. Yeah. So, yeah, just, yeah, you can… it's still in a draft, so we…
Marius Ciocanel 00:58:06 Yeah, I'll prove that.
Nacho Bonafonte 00:58:07 But, yeah. We can try that, yeah, you can move that. We're ready, and we can try to fix. Okay, let's go to the next one, because we are a bit short on time.
Yeah, update the sub-support for metric kit. I think this is also a new one.
Yeah, and… and it needs… Oh, it's a… it's a work in progress.
And he's asking… Yeah, probably if you want to review and add some feedback on this, I don't know why… Oh, there is also support on Mac now?
yeah, I've done… Oh, they need… compiler 6.4?
That's two species, right? Why would you need 6 for Swift for this?
Yeah, that's how it suits PCOS.
Ben Joseph 00:59:20 I think this is specific to the changes, with… for Metricade in 27.
Nacho Bonafonte 00:59:28 They need, they need later Swift.
Ben Joseph 00:59:32 I… so, iOS 27 has changes with respect to metric kit.
Okay. Like, some, some behavior changes.
So are… are these… I did not review it, I'm just asking, like, maybe this is, specific for that, like, the older behavior is still maintained, but… For 27 and newer, I think we need additional,
Nacho Bonafonte 00:59:58 report streams on iOS 27 and newer.
Reporter's trims.
And those streams are… Okay… Yeah, that's interesting to check.
Maybe, what… what's newer on 6.4?
for streams.
Maybe a spam?
But the spanse was previous, right?
Yeah, no, it's heavy.
Yeah.
I don't know. Yeah, that's… yeah, we should test it, yeah, because…
Ben Joseph 01:00:39 Yeah.
Nacho Bonafonte 01:00:40 Yeah. But, from what I can see, just…
Ben Joseph 01:00:43 Yeah, it's only additive, it does not remove or change anything for previous versions.
Only for the newer version, this is, like, adding some, behavior, yeah.
Nacho Bonafonte 01:00:54 Yeah, but I don't know why not 6'3", for example. I don't know, that's the only… maybe… I don't know what functionality is needed then, 6.4, that… If not before.
And only supported on 27. I mean, I can understand the 27 only, for some Mac support, but… Yeah, there's… compiler version is what is a bit more suspicious here, but maybe it's something we cannot do. And even then.
I don't know if…
Marius Ciocanel 01:01:24 I mean, it's a.
Nacho Bonafonte 01:01:25 Which we can also…
Marius Ciocanel 01:01:25 Kim.
Nacho Bonafonte 01:01:26 Yeah, yeah, that's right, yeah, totally. Even then, I don't know why… We should do it here, and not in the… Inside the method, right?
Yeah, okay.
Okay, that… Oh, we are out of time. And this is about distributed tracing. I think you already approved that. Okay, that's a good one. And we are done.
Okay, yeah, that's all for the week.
Thank you all.
For coming to the meeting.
Yeah, let's… Have a nice weekend, and see you next week.
Ben Joseph 01:02:10 Thank you.
Billy Billy 01:02:11 Thank you, everyone.
Ben Joseph 01:02:11 Bye. Bye.
Marius Ciocanel 01:02:12 See you later on next week. Bye.
