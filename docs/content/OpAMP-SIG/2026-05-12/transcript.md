SIG: OpAMP SIG
Date: 2026-05-12
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/CXU0r6kS6rscMA1Q7VVc6JYrppbQ_qp6ibbJn1_SuIj6ObfoHsKDHc4kxa1E4kh9.joHBlECk54pMzyYs
============================================================

## Zoom Recording Transcript

**Andy Keller** 05:56 Hey.
**Evan Bradley** 05:59 Hello?
I think we're good to get started. Stanley, you can go ahead, you've got the first item.
**Stanley Liu** 06:39 Sure, thanks.
Yeah, so I am just following up on the message attestation work that I raised a few SIG meetings ago.
I got feedback that, we would probably be good to proceed, but wanted to see, what the implementation would look like, how complex it might be, so I shared a draft PR for the proof of concept.
It's pretty much complete, so we just want to get feedback.
If there's any reviews or comments or concerns before proceeding and opening it up for, like, official review, so… I've also linked the, proposal document in the PR as well.
Yeah, not sure if anyone had any, like.
Existing concerns about it, but just wanted to reshare, and then get some feedback over the next few weeks.
**Andy Keller** 07:48 Yeah, just… thanks, thanks for… bringing it to my attention. I guess he just posted it 34 minutes ago, so… I didn't miss anything, but .
**Stanley Liu** 07:57 Yeah.
**Andy Keller** 07:58 I mean, just skimming it, overall, like, structure and everything looks good.
I'll get into the details and, fight some feedback.
**Stanley Liu** 08:08 Cool, thanks.
**Evan Bradley** 08:18 Okay, I've got the second item. This is the fallback configuration, or startup fallback configuration, just to give it all of the qualifiers, Pierre, that Douglas has had open for a little while now.
I think we've kind of whittled it down to a good set of functionality. It looks good to me, but I wouldn't mind if, somebody could put a second pair of eyes on it.
Just make sure that we're not missing anything. If not, I'll merge it by next Wednesday. I just wanted to put out the request.
**Dakota Paasman** 08:55 Yeah, I, I think the last SIG meeting, I decided to review it, and I did not get a chance to do that, so sorry about that. I will make sure I review it this afternoon.
**Evan Bradley** 09:05 All good. Thank you.
Definitely. You got the next item?
**Dakota Paasman** 09:11 Yeah, so I just opened this up a little bit ago, This came out of some PR review that Tgrin left on… my first, supervisor upgrades PR, basically… the main function responsible for, actually doing the update needs to know what kind of package we're handling. So the current OpAM Go implementation has a file downloader that, will actually download the data from the URL that's passed in the package is available, request or message. Anyways, it reads this package and then puts it into a IO.reader, for this updateContent function to read from.
The issue with that is it doesn't know what kind of package is in there.
Whether or not it's compressed, it needs to be decompressed, or if it's a specific, archive type, etc.
So, in the first supervisor Upgrades PR, I had this idea of a config parameter that the user would specify for the package, and say, you know, for upgrades, this is the package type that's expected.
Tigran left some review that instead we should pass the download URL to the updateContent function so that it can… Kind of sniff out the package type based on the URL.
I think that works in most cases, This just needs to be reviewed.
There is one edge case I kind of stumbled across. I'm not super familiar with them.
But for a signed CDN URL, you know, the… The package type is… kind of… hidden, you know, it's just a random protected URL.
So we're not gonna be able to infer the package type based on that.
I feel like that's a pretty valid use case for a package upgrade, to send it with that kind of URL, essentially.
**Andy Keller** 11:23 I'm not sure I totally… Get what you mean. You're just saying because the URL might be…
**Dakota Paasman** 11:30 Yeah, like, the URL might not contain the actual… Package name that was downloaded, so we can't infer the package type.
Based on the…
**Andy Keller** 11:40 But we should be able to use… response headers, right? So, for, like, content encoding, content type.
**Dakota Paasman** 11:48 Yeah, if those are set, that would be… I suppose then a different parameter that we should pass to this function.
You know, instead of the URL, we could pass, like, the content type header, if it's set.
**Andy Keller** 12:03 I guess I was thinking… sorry, I don't know the full details.
I guess I was thinking, you know, you would download When you download this, you would get… That response, and That would just be kind of baked into, you know, a normal web request, like, like we're… That it would… Unzip it, if it's compressed, it would… Yeah, I don't… I don't know, I guess I have to think about it some more, like, what the specific issues are, but… Yeah, I don't know. I don't think I'll stop right now.
But I'm not sure that… I guess I'm just not sure that that case is an issue.
**Michel Laterman** 12:58 Just for my knowledge, with the package names, that it uses be, like, Collector or collector.car.gzv or something?
**Dakota Paasman** 13:10 Yeah, so it could be that. You know, the… The happy path that we're trying to solve for with this is, like.
you're passing the hotel collector releases repo, you're passing that package to the supervisor, which would be, I think it's, like, hotel call.
the OS, and then the architecture.tar.gz, and then inside of that is the collector, and maybe a license. I think there's some other stuff.
**Michel Laterman** 13:44 Yeah, but if… If you're passing a package name that has par.gz, can't we just use that to know Use Jesus abused her.
**Dakota Paasman** 13:57 Oh, like…
**Michel Laterman** 13:59 Yeah.
**Dakota Paasman** 13:59 In the configuration of the supervisor?
Or…
**Andy Keller** 14:04 It's just saying detect the file name of the URL.
**Michel Laterman** 14:07 Yeah.
**Dakota Paasman** 14:08 Yeah, yeah, that's, that's… that's the, you know, that is the common case that this would solve, like, that's what it would be used for. I'm raising, like, the edge case scenario when that isn't what the URL has.
**Michel Laterman** 14:23 I mean, right now, the… Your pure… is adding… An argument after package name.
My question is specifically, what is package name?
Does it? I'm getting…
**Dakota Paasman** 14:38 Package name is the name… Package name is the name of the binary that's in the archive that's downloaded.
**Michel Laterman** 14:46 Okay, okay.
**Dakota Paasman** 14:47 Sorry, yeah.
**Michel Laterman** 14:49 Yeah.
**Dakota Paasman** 14:49 I wasn't Yeah, so it does, it doesn't contain the package type in it, you know, the tar.gz or whatever else it might be.
Nope.
So… We don't need to… discuss this a ton right now, or get, you know, super in the weeds on it. I just wanted to raise this.
So, happy to… Continue talking on Slack, or… In the PR.
But that is all I have.
**Andy Keller** 15:31 Okay, thanks, Jacob.
**Michel Laterman** 15:48 Yeah, so I have the next one.
Mines coming from… A request from one of my colleagues who's trying to integrate The health check extension with All-PAMP components.
Health reports.
And he's running into an issue where the extension reports attributes, but RSpec doesn't have those part of component all statuses.
So, we just like to make it consistent with the extension.
To make our dilution easier.
So, adding it to the spec should be a… One line change.
**Andy Keller** 16:31 Yeah, sure.
That seems reasonable to me. I don't… I don't… I'm not familiar with the… what health check reports in attributes, But I think aligning it with… Whatever it is, it should be aligned.
Do you know, do you know what's commonly in there?
**Michel Laterman** 16:54 No. I don't really have it.
**Evan Bradley** 16:59 So, I can answer that.
**Andy Keller** 17:01 Yeah, it's.
**Evan Bradley** 17:02 like, updates about the components. The component might say, like, you know, the OTLP receiver started on this port, stuff like that.
So the message might be, like, OTLP receiver started, and attributes might be, like, you know, receiver name and, you know, address and port number, or something along those lines.
**Juande Manjon** 17:24 So…
**Evan Bradley** 17:24 Yeah, I mean, I think it probably makes sense to include these. I think a map of attributes is… I don't know, fairly generically useful, I would think somewhat non-controversial, but… Yeah, I think in general, we should try to align with the component health events where we can.
**Michel Laterman** 17:47 What's…
**Andy Keller** 17:47 Yeah.
**Michel Laterman** 17:48 I'll make a PR for the spec change.
**Juande Manjon** 17:55 This set of attributes in the heart checks are interesting, where we can leverage to send heartbeat information from the particular component.
Specifically, you specify signed state.
That the consumer and the producer know.
There is a lack on the any value, because at the end, it rely on the key value, and the value is any value, and the value has bytes, so bytes, you can send anything you like, but if we can add a new… any protobar field that contains the class or the message.
a name and the byte could be more powerful to send. In that case, the sender and the receiver know how to decode that particular message. If not, we… I need to… if we are extending this attribute to send this heartbeat or any special information associated with the health.
So, we need to find artifacts to identify which method.
Type is sent in the bytes.
In any value.
to… maybe I'm thinking we can extend that, so it could be a change in the spec.
I will try to provide more information about what is needed and how. After this new attribute in the health check is Accept it.
**Andy Keller** 19:25 Okay.
We'll put a thumbs up on this as well.
Do you have a… do you have a PR, Michael, or not yet?
**Michel Laterman** 19:42 Not yet. I'll write one, it should be quick.
**Andy Keller** 19:45 I think it'll be 3 lines, officially, but Well, I guess the proto needs to be updated as well, but… so, it'll be… it'll be a couple lines, but yeah, just… just let me know. I think it sounds… Good to me. I might, I might just let Tigran take the review of it so that he has some visibility, but, since he's not here… Yep.
I don't think there's any objections from anyone here.
Anything else?
**Juande Manjon** 20:43 Yeah, so, I'm trying to find someone else to co-sponsor the open country repo that I was trying to… to do, to help a user to adopt, OPAM.
I couldn't find any, so I cannot try to send a broader message in the Slack channel to see someone else step up, and we can at least start the process in case of… We find someone else to… to try to have this country repo.
Where we can move the internals into the country repo, so… We can use that, To provide better server and agent capability for, like, you know, helping people to… how to use a pan in the film.
**Andy Keller** 21:41 Yeah, I guess I'm not… I know Tigran felt pretty strongly that we needed to have another sponsor before we move forward, So I… I certainly would want to include him in this discussion.
**Juande Manjon** 22:00 So, yeah, so meanwhile, I'm gonna try to send the message to see someone else.
**Andy Keller** 22:04 Okay.
**Juande Manjon** 22:05 Join.
**Andy Keller** 22:06 Okay.
**Juande Manjon** 22:10 That's all from me.
**Evan Bradley** 22:30 Alright, anything…
**Andy Keller** 22:31 Looks like that's it. I can, I'm kind of curious if everybody has any thoughts on this. I, I, I have a little bit of a crazy architecture, I just, was developing for… it's not crazy.
It's a toy. It's reasonable, but for a customer use case.
That I thought I'd just share.
Now that we can support, extensions in the supervisor, I think… I've talked about the OutBAMP Gateway extension before, but it basically allows you to relay Out BAMP messages.
We can actually put the op-amp gateway extension in the supervisor itself, and allow… child… collectors to connect to that supervisor, and then have a single upstream message.
to the server, Kind of the normal… The normal use case would be this, where you have the extension running in the collector, but then you have Upstream op-amp connection from the extension, and a separate one from the supervisor.
So… I'm just curious, I don't know if anybody found that interesting, or useful, or, If anybody has a use case that's similar to that.
**Evan Bradley** 24:00 Just from an architectural standpoint, I really like this. Just the way that it segments the, like, control plane and telemetry ingestion layers of the architecture.
**Douglas Camata** 24:13 And also, this reminds me of the KubeCon EU conversations regarding having some sort of bridge similar to the one that the operator has, but that That works with collector configurations directly. So, to me, this seems… this… Relates a bit, because you have this one kind of gateway Supervisor. Seems, seems cool.
**Andy Keller** 24:41 Yeah, the only… the only downside, I think, is that the OpAmp Gateway is… It's, it's, you know, fairly small, but it's, you know, adds complexity to the supervisor.
And so there is a risk that, you know, the supervisor goes down, And then… you know, then you lose your connection, your opium connection. That's kind of the whole point of the supervisor, is to be this… Tight little thing that, is always running and, isn't, You know, it isn't subject… subjected to all the complexity of the collector itself.
So this, you know, breaks out a little bit, but I think, I think it's pretty useful, so…
**Evan Bradley** 25:32 Could we… maybe wrap extensions in something that catches panics or something like that, if we're concerned about stability? I mean, the nice thing about this is that if we use extensions, it's… the complexity is segmented off.
Right. It's not like it's in the main, like, supervisor process management code.
But I wonder if we can do something like just catch panics in… Maybe that would kind of alleviate some of the concerns around… I don't know where this would panic, because, I mean, it should be fairly routine, I think? I mean, maybe on, like, proto-decoding or something.
**Andy Keller** 26:08 Yeah, well, I think if you look at the Opium Gateway extension implementation, it's in our repo, in our hotel contribo, but, By Plain Hotel Contrib and the ObserveIQ org.
You know, it maintains upstream connections, downstream connections, and has to… Relay those messages across channels, and, you know, there's always a… possible situation of a deadlock or something like that.
Where I would like to think that my code is perfect, and that is… impossible. But, you know, that's where, like, the complexity lies.
And, you know, something like that happening, or… or exhausting… Connections, or something like that.
You know, is where you could run into issues.
again, I think, you know, cleanup is good, everything's perfect, no bugs, but we can't upgrade the supervisor or the extension that runs in it, so… That's… that's where the risk, I think, lies.
**Douglas Camata** 27:12 Extensions are cool, but they… and the downside is that I think they will always have some risk, right? Not only panics, but all these other things that Andy mentioned, like… deadlocks, issues with connections… I don't know, maybe they will have a memory leak, and .
**Andy Keller** 27:32 Right.
**Douglas Camata** 27:33 Or, or other issues.
**Andy Keller** 27:35 All those things, yeah, yeah.
Yeah, so, like I said, I think the Opium Gateway extension is a pretty small piece of code, pretty tight, you know, isn't… is it leaking… leaking as far as I can tell? Hasn't it locked? You know, etc. But that's sort of the risk of that architecture.
But the benefit is that you have this nice single upstream connection.
And you've… you're now managing downstream hosts.
So… No.
Well, cool, thanks.
I'll probably put together a blog or something on that, so you can actually see how it's… how everything's wired together, but it, you know, like, works today, so… It works with Dakota's PR, that's extension support, I don't know where that PR code… That's still a good question.
**Douglas Camata** 28:38 That's gonna be a really good showcase of what can be possible with extensions in the supervisor. Maybe it will bring some creativity to other people as well, too.
to build.
**Andy Keller** 28:50 Yeah, I mean, the intention was really auth extensions and, you know, OAuth support, and then, as I was contemplating this, I was like, I think this is possible. All I really need to do is, like, start and stop this thing, so… So… Yeah.
Cool, alright.
Well, if that's it, I guess we'll see you in two weeks.
Unless anybody has anything else?
Alright.
See ya.
